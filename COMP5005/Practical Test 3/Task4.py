# !pip install matplotlib numpy

import numpy as np
import matplotlib.pyplot as plt
import random

class House:
    def __init__(self, pos, colour, size):
        self.pos = pos
        self.colour_code = colour
        self.size = size

    def get_image(self):
        s = self.size
        img = np.ones((s, s * 2)) * self.colour_code
        return img

    def get_topleft(self):
        xleft = self.pos[0] - self.size // 2
        ytop = self.pos[1] - self.size // 2
        return (xleft, ytop)

class Tree:
    def __init__(self, pos, colour, size):
        self.pos = pos
        self.colour_code = colour
        self.size = size

    def get_image(self):
        s = self.size
        img = np.ones((s, s)) * self.colour_code
        return img

    def get_topleft(self):
        xleft = self.pos[0] - self.size // 2
        ytop = self.pos[1] - self.size // 2
        return (xleft, ytop)

class Block:
    def __init__(self, size, topleft):
        self.size = size
        self.topleft = topleft
        self.items = []
        self.draw_border()  
        
    def add_item(self, item):
        self.items.append(item)

    def generate_image(self):
        grid = np.zeros((self.size, self.size))
        for item in self.items:
            topleft = item.get_topleft()
            img = item.get_image()
            cx_start = topleft[0]
            ry_start = topleft[1]
            cx_stop = cx_start + img.shape[1]
            ry_stop = ry_start + img.shape[0]
            if 0 <= ry_start < self.size and 0 <= cx_start < self.size:
                grid[ry_start:ry_stop, cx_start:cx_stop] = img[:, :]
        return grid

    def draw_border(self):
        x = self.topleft[0]
        y = self.topleft[1]
        plt.plot([x, x + self.size, x + self.size, x, x], [y, y, y + self.size, y + self.size, y], color='red')

def generate_image(blocks, block_size, grid_shape):
    grid = np.zeros((grid_shape[0] * block_size, grid_shape[1] * block_size))
    for block in blocks:
        (cx_start, ry_start) = block.topleft
        grid[ry_start:ry_start + block_size, cx_start:cx_start + block_size] = block.generate_image()
    return grid

def main():
    block_size = 25
    grid_shape = (2, 3)  
    blocks = []

    plt.figure(figsize=(10, 5))
    # Create blocks in a 2x3 grid
    for i in range(grid_shape[0]):
        for j in range(grid_shape[1]):
            topleft = (j * block_size, i * block_size)
            block = Block(block_size, topleft)

            if i == 0:
                block.add_item(Tree((3, 4), 2, 4))
                block.add_item(Tree((7, 20), 3, 4))
                block.add_item(Tree((18, 5), 3, 6))
                block.add_item(House((10, 13), random.randint(7, 10), 6))
            else: 
                block.add_item(Tree((random.randint(3,18), random.randint(3,18)), random.randint(3,6), random.randint(2,6)))
                block.add_item(Tree((random.randint(3,18), random.randint(3,18)), random.randint(3,6), random.randint(2,6)))
                block.add_item(Tree((random.randint(3,18), random.randint(3,18)), random.randint(3,6), random.randint(2,6)))
                block.add_item(Tree((random.randint(3,18), random.randint(3,18)), random.randint(3,6), random.randint(2,6)))
                block.add_item(Tree((random.randint(3,18), random.randint(3,18)), random.randint(3,6), random.randint(2,6)))

            blocks.append(block)

    img = generate_image(blocks, block_size, grid_shape)
    plt.imshow(img, vmin=0, vmax=10)
    plt.colorbar()
    plt.title('Task 4: (2, 3) Grid of blocks with houses and trees')
    plt.savefig("task4.png")
    plt.show()

if __name__ == "__main__":
    main()
