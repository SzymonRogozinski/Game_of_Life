
class Game:

    def __init__(self, height, width, iteration_number, iterations, threads):
        self.height = height
        self.width = width
        self.iteration_number = iteration_number
        self.iterations = iterations
        self.threads = threads


class Iteration:

    def __init__(self, height, width):
        self.plane = [[False for _ in range(width)] for _ in range(height)]

