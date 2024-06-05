from Gui import Gui
from mpi4py import MPI

class Game:

    direction = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]

    def __init__(self, height, width, iteration_number):
        self.height = height
        self.width = width
        self.iteration_number = iteration_number
        self.iterations = []

    def load_data(self, filename):
        i = Iteration()
        i.load_file(filename)
        self.iterations.append(i)

    def simulation(self):
        comm = MPI.COMM_WORLD
        id = comm.Get_rank()  # number of the process running the code
        num_processes = comm.Get_size()  # total number of processes running
        # Create range for threads
        if id == 0:
            indexes = []
            package_size = (self.height-2)//num_processes
            for i in range(num_processes):
                indexes.append([i*package_size, i*package_size+package_size+1])
            if not indexes[-1][1] == self.height-1:
                indexes[-1][1] = self.height - 1
        # Do self.iteration_number iterations
        for _ in range(0, self.iteration_number):
            packages = []
            # Pack data
            if id == 0:
                packages = self.__make_packages(indexes)
            data = comm.scatter(packages, root=0)
            # Create output data
            result_package = Pack([[False for _ in range(self.width)] for _ in range(len(data.content))], data.id)
            for i in range(1, len(data.content)-1):
                for j in range(1, self.width-1):
                    result_package.content[i][j] = self.__count_neighbour(j, i, data)
            results = comm.gather(result_package, root=0)
            # Connect data to one place
            if id == 0:
                sorted(results, key=lambda x: x.id)
                packed = []
                packed.append(self.iterations[-1].plane[0])
                for res in results:
                    packed.extend(res.content[1:-1])    # Ignore first and last line (redundant)
                packed.append(self.iterations[-1].plane[-1])
                iteration = Iteration()
                iteration.set(packed)
                self.iterations.append(iteration)
                #print(self.iterations)
        if id == 0:
            gui = Gui(self.width, self.height, self.iterations)
            gui.display();

    def __count_neighbour(self, x, y, data):
        old_iter = data.content
        count = 0
        for dir in self.direction:
            if old_iter[y+dir[0]][x+dir[1]]:
                count += 1
        return (old_iter[y][x] and 1 < count < 4) or (not old_iter[y][x] and count == 3)

    def __make_packages(self, indexes):
        i = 0
        packages = []
        iteration = self.iterations[-1]
        #iteration.print(len(self.iterations)-1)
        for index in indexes:
            d = [iteration.plane[j] for j in range(index[0], index[1]+1)]
            p = Pack(d, i)
            packages.append(p)
            i += 1
        return packages


class Iteration:

    def __init__(self):
        self.plane = []

    def load_file(self, filename):
        with open(filename, "r") as file:
            self.plane = [[s == "1" for s in line[:-1]] for line in file.readlines()]

    def set(self, plane):
        self.plane = plane

    def print(self, iteration_number):
        print(f"\nIteration number {iteration_number}\n")
        for line in self.plane:
            line_string = ""
            for cell in line:
                if cell:
                    line_string += "X"
                else:
                    line_string += "O"
            print(f"{line_string}")


class Pack:

    def __init__(self, content, number):
        self.content = content
        self.id = number
