import matplotlib.pytplot as plt
import numpy as np
import math

x = np.array([1,2,3,4,5,6])
y = np.array([1,3,6,7,2,1])

x2 = np.arange(0, 2 * math.pi, 0.01)
y2 = np.sin(x2)

plt.plot(x, y)
plt.show()