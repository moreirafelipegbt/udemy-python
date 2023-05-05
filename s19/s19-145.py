#import Numpy Library
import numpy as np
#Create a numpy array from a list
array = np.array([1,2,3,4,5])
#It is possible to store many types in a Numpy list
try:
    array2 = np.array(['item1', 2, True])
    print(array2)
except Exception as err:
    print('Err {}', err)
#Update values based on indexes
array[0] = 0
print(array)
#Insert new items with insert()
array = np.insert(array, 0, 30)

print(array)


