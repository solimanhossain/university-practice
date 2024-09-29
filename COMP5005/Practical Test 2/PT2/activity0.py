import numpy as np
import matplotlib.pyplot as plt


numrows = 8
numcols = 10

x_ones = np.ones(numrows+1)
y_range = np.arange(0, numrows+1)
y_ones = np.ones(numcols+1)
x_range = np.arange(0, numcols+1)

plt.plot(x_ones, y_range)
plt.plot(x_range, y_ones)

plt.show()

