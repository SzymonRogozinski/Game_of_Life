from GameStructures import Game

if __name__ == '__main__':
    g = Game(40, 40, 1000)
    g.load_data("data.txt")
    g.simulation()
    print(g)
