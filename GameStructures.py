
class Game:

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


class Iteration:

    def __init__(self, height, width):
        self.plane = [[False for _ in range(width)] for _ in range(height)]

    def load_file(self, filename):
        with open(filename, "r") as file:
            self.plane = [[s == "1" for s in line[:-1]] for line in file.readlines()]
