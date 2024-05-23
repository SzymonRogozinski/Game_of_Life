from GameStructures import Game

if __name__ == '__main__':
    g = Game(10, 10, 5)
    g.load_data("data.txt")
    g.simulation()
    print(g)
