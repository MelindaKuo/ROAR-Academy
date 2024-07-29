import matplotlib.pyplot as plt
import os
import numpy as np


y_points = np.array([2,4,1])
x_points = np.array([1, 2, 3])


plt.ylim(1.0, 4.0)
plt.xlim(1.0, 3.0)


plt.xticks(np.arange(1.0, 3.1, 0.5),['1.0', '1.5', '2.0', '2.5', '3.0'])


plt.plot(x_points, y_points)
plt.show()