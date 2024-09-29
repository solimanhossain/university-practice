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

def subplot_trees(ax, title, cmap=None):
    xlim, ylim = 60, 80
    grid = np.zeros((ylim,xlim))
    grid[0,0] = 10
    im = ax.imshow(grid, cmap=cmap)
    plt.colorbar(im, ax=ax)
    c = 'g' if cmap else 'r'
    s = 40 if cmap else 20
    clr = 'yellow' if cmap else 'green'

    for step in range(20):
        tree = Tree((random.randint(20, xlim-20),random.randint(20, ylim-20)), c, s)
        ax.scatter(tree.get_coord()[0], tree.get_coord()[1], c=tree.get_colour(), s=tree.get_size())

    ax.add_patch(Rectangle(xy=(10, 10), width=40, height=60, linewidth=4, color=clr, fill=False))
    # ax.grid(True, color=clr)
    ax.set_title(title)

def main():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    subplot_trees(ax1, 'Task 1: Random Red Trees')
    subplot_trees(ax2, 'Task 2: Random Green Trees', 'hot')

    plt.suptitle('TWO TREE PLOTS', fontsize=16)
    plt.savefig("task2.png")
    plt.show()

if __name__ == "__main__":
    main()