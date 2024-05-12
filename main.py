from GameStructures import Game

if __name__ == '__main__':
    g = Game(5, 5, 5, 1)
    g.load_data("data.txt")
    g.simulation()
    print(g)
