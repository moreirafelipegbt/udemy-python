import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5,6])
y = np.array([1,3,6,7,2,1])

custom_font = {'family': 'serif', 'color': '#339FFF', 'size': 17}

plt.xlabel("This is 'x'")
plt.ylabel("This is 'y'")
plt.title('Plotting y=f(x)', fontdict=custom_font)

#makers - we can emphasize the data points
plt.plot(x, y, marker='o', ms=13, mec='red', mfc='green', lineweight=)
plt.show()