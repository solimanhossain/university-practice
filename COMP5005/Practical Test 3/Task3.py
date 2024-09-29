# !pip install matplotlib numpy

import random
import numpy as np
import matplotlib.pyplot as plt


class House():
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

class Tree():

    def __init__(self, pos, colour, size):
        self.pos = pos
        self.colour_code = colour
        self.size = size     

    def get_image(self):
        s = self.size
        img = np.ones((s,s)) * self.colour_code #row_y/col_x
        return img

    def get_coord(self):
        return self.pos

    def get_topleft(self):
        xleft = self.pos[0] - self.size//2
        ytop = self.pos[1] - self.size//2
        return (xleft,ytop)

    def get_size(self):
        return self.size

    def get_colour(self):
        return self.colour_code


class Block():

    def __init__(self, size, topleft):
        self.size = size        
        self.topleft = topleft  
        self.items = []         

    def get_topleft(self):
        return self.topleft

    def add_item(self, item):
        self.items.append(item)

    def generate_image(self):
        grid = np.zeros((self.size,self.size))

        for item in self.items:
            topleft = item.get_topleft() 
            img = item.get_image()       
            cx_start = topleft[0]
            ry_start = topleft[1] 
            cx_stop = cx_start + img.shape[1]
            ry_stop = ry_start + img.shape[0]
            grid[ry_start:ry_stop,cx_start:cx_stop] = img[:,:] 
        return grid

def generate_image(b, s, mshape):
    grid = np.zeros((mshape[0]*s, mshape[1]*s))
    for block in b:
        (cx_start,ry_start) = block.get_topleft()
        grid[ry_start:ry_start+s,cx_start:cx_start+s] = block.generate_image()[:,:]
    return grid

def main():
    blocksize = 25 
    map_shape = (1, 1) 
    blocks = []

    block = Block(blocksize, (0, 0))
    block.add_item(Tree((4, 4), 3, 3))
    block.add_item(Tree((17, 2), 5, 2))   
    block.add_item(Tree((5, 16), 3, 4))
    block.add_item(Tree((20, 20), 5, 2))

    block.add_item(House((8, 10),  10 , 5)) 

    blocks.append(block)

    plt.imshow(generate_image(blocks, blocksize, map_shape), vmin=0, vmax=10)
    plt.colorbar()
    plt.title('Task 3: Testing Blocks with Trees and House')
    plt.savefig("task3.png")
    plt.show()

if __name__ == "__main__":
    main()

