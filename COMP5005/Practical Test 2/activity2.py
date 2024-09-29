# !pip install numpy
# !pip install matplotlib

import numpy as np
import matplotlib.pyplot as plt

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
    plt.plot(x_range, y_full, color='red')

for row in range(numrows):
    for col in range(numcols):
            rev_row = numrows - row - 1
            rev_col = numcols - col - 1
            plt.annotate(f'{rev_row},{col}', (col, row), fontsize=8)

plt.title('Activity 2')
plt.show()


