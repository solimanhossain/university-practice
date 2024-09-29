# !pip install matplotlib numpy

import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

class Tree():
    def __init__(self, pos, colour, size):
        self.pos = pos
        self.colour_code = colour
        self.size = size

    def get_coord(self):
        return self.pos

    def get_size(self):
        return self.size

    def get_colour(self):
        return self.colour_code

def main():
    xlim, ylim = 60, 80
    grid = np.zeros((ylim,xlim))

    grid[0,0] = 10
    plt.imshow(grid)
    plt.colorbar()
    # plt.grid(True)

    for step in range(10):
        tree = Tree((random.randint(20, xlim-20),random.randint(20, ylim-20)), 'r', 100)
        plt.scatter(tree.get_coord()[0], tree.get_coord()[1], c=tree.get_colour(), s=tree.get_size())

    currentAxis = plt.gca()
    currentAxis.add_patch(Rectangle(xy=(10, 10), width=40, height=60, linewidth=5, color='green', fill=False))

    plt.title('Task 1: Random Red Trees')
    plt.savefig("task1.png")
    plt.show()

if __name__ == "__main__":
    main()