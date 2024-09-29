# !pip install numpy
# !pip install matplotlib

import numpy as np
import matplotlib.pyplot as plt

numrows = 10
numcols = 8

for col in range(numcols+1):
    x_full = np.full(numrows+1,col)
    y_range = np.arange(0, numrows+1)
    plt.plot(x_full, y_range, color='black')

for row in range(numrows+1):
    y_full = np.full(numcols+1,row)
    x_range = np.arange(0, numcols+1)
    plt.plot(x_range, y_full, color='red')

plt.annotate('(1,1)', (1, 1))

plt.title('Activity 1')
plt.show()
