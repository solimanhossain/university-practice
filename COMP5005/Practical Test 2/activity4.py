# !pip install numpy
# !pip install matplotlib

import numpy as np
import matplotlib.pyplot as plt

sizes = [10, 20, 30, 40]
colors = ['darkgreen', 'green', 'lightgreen']

print("Enter the value between 5 to 20.")

while True:
    numrows = int(input("Rows: "))
    numcols = int(input("Columns: "))
    if 4 < numrows < 21 and 4 < numcols < 21: break

for col in range(numcols+1):
    x_full = np.full(numrows+1,col)
    y_range = np.arange(0, numrows+1)
    plt.plot(x_full, y_range, color='black')

for row in range(numrows+1):
    y_full = np.full(numcols+1,row)
    x_range = np.arange(0, numcols+1)
    plt.plot(x_range, y_full, color='black')

for row in range(numrows):
    for col in range(numcols):
            size = sizes[col % len(sizes)]
            color = colors[col % len(colors)] 
            plt.scatter(col + 0.5, row + 0.5, color=color, s=size)

plt.title('Activity 4')
plt.show()
