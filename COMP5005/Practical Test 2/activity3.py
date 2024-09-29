# !pip install numpy
# !pip install matplotlib

import numpy as np
import matplotlib.pyplot as plt

colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']

print("Enter the value between 5 to 20.")

while True:
    numrows = int(input("Rows: "))
    numcols = int(input("Columns: "))
    if 4 < numrows < 21 and 4 < numcols < 21: break


for col in range(numcols+1):
    x_full = np.full(numrows+1,col)
    y_range = np.arange(0, numrows+1)
    plt.plot(x_full, y_range, color=colors[col % len(colors)])

for row in range(numrows+1):
    y_full = np.full(numcols+1,row)
    x_range = np.arange(0, numcols+1)
    plt.plot(x_range, y_full, color=colors[row % len(colors)])

for row in range(numrows):
    for col in range(numcols):
            color = colors[col % len(colors)] 
            plt.scatter(col + 0.5, row + 0.5, color=color)

plt.title('Activity 3')
plt.show()


