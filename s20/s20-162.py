#Subplots
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5,6])
y = np.array([1,3,6,7,2,1])

#We will have 1 row and 2 cols (and actual one is the first one)
plt.subplot(2, 2, 1)
plt.plot(x,y)
plt.title('First plot')

#This is the second plot
plt.subplot(2, 2, 2)
plt.plot(y, x)
plt.title('Second plot')

#This is the third plot
plt.subplot(2, 2, 3)
plt.plot(y, x)
plt.title('Third plot')

#This is the fourth plot
plt.subplot(2, 2, 4)
plt.plot(y, x)
plt.title('Fourth plot')

plt.suptitle('GROUP OF PLOTS')
plt.show()