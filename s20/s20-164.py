import matplotlib.pyplot as plt
import numpy as np
import math

# Toyota models age and top speed
x = np.array([1, 4, 6, 8, 10, 15, 20])
y = np.array([200, 180, 190, 150, 170, 130, 100])
plt.scatter(x, y, color='green')

# Hyundai models age and top speed
x2 = np.array([2, 4, 5, 9, 10, 13, 18])
y2 = np.array([190, 175, 132, 176, 112, 80, 95])
plt.scatter(x2, y2, color='orange')

plt.title('CARS AGE-TOP SPEED DIAGRAM')
plt.xlabel('Age')
plt.ylabel('Top Speed')

#This is how we show the color codes (in this case brands)
plt.legend(labels=['Toyota', 'hyundai'], loc='upper right')

plt.show()