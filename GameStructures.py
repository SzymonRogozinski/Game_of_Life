
class Game:

    direction = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]

    def __init__(self, height, width, iteration_number, threads):
        self.height = height
        self.width = width
        self.iteration_number = iteration_number
        self.iterations = []
        self.threads = threads

    def load_data(self, filename):
        i = Iteration(0, 0)
        i.load_file(filename)
        self.iterations.append(i)

    def simulation(self):
        for _ in range(0, self.iteration_number):
            new_iter = Iteration(self.height, self.width)
            self.iterations.append(new_iter)
            for i in range(1, self.height-1):
                for j in range(1, self.width-1):
                    new_iter.plane[i][j] = self.__count_neighbour(j, i)

    def __count_neighbour(self, x, y):
        old_iter = self.iterations[-2].plane
        count = 0
        for dir in self.direction:
            if old_iter[y+dir[0]][x+dir[1]]:
                count += 1
        return (old_iter[y][x] and 1 < count < 4) or (not old_iter[y][x] and count == 3)


class Iteration:

    def __init__(self, height, width):
        self.plane = [[False for _ in range(width)] for _ in range(height)]

    def load_file(self, filename):
        with open(filename, "r") as file:
            self.plane = [[s == "1" for s in line[:-1]] for line in file.readlines()]
