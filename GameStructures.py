from mpi4py import MPI

class Game:

    direction = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]

    def __init__(self, height, width, iteration_number):
        self.height = height
        self.width = width
        self.iteration_number = iteration_number
        self.iterations = []

    def load_data(self, filename):
        i = Iteration(0, 0)
        i.load_file(filename)
        self.iterations.append(i)

    def simulation(self):
        comm = MPI.COMM_WORLD
        id = comm.Get_rank()  # number of the process running the code
        num_processes = comm.Get_size()  # total number of processes running
        if id == 0:
            indexes = []
            package_size = (self.height-2)//num_processes
            for i in range(1, self.height-1, package_size):
                indexes.append([i-1, i+package_size+1])
            if not indexes[-1][1] == self.height-1:
                indexes[-1][1] = self.height - 1

        for _ in range(0, self.iteration_number):
            packages = []
            if id == 0:
                packages = self.__make_packages(indexes)
            data = comm.scatter(packages, root=0)
            result_package = Package([[False for _ in range(self.width)] for _ in range(len(data))], data.id)
            for i in range(1, len(data) -1):
                for j in range(1, self.width-1):
                    result_package.content[i][j] = self.__count_neighbour(j, i, data)
            results = comm.gather(result_package, root=0)
            if id == 0:
                sorted(results, key=lambda x: x.id)
                packed = []
                for res in results:
                    packed.extend(res.content[1:-1])
                iteration = Iteration(0, 0)
                iteration.set(packed)
                self.iterations.append(iteration)

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
        for index in range(len(indexes)):
            packages.append(Package([self.iterations[-1].plane[j] for j in range(index[0], index[1])], i))
            i += 1
        return packages


class Iteration:

    def __init__(self, height, width):
        self.plane = [[False for _ in range(width)] for _ in range(height)]

    def load_file(self, filename):
        with open(filename, "r") as file:
            self.plane = [[s == "1" for s in line[:-1]] for line in file.readlines()]

    def set(self, plane):
        self.plane = plane


class Package:

    def __int__(self, content, number):
        self.content = content
        self.id = number
