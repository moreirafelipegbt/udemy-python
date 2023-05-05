import numpy as np

array = np.array([[1, 2 , 3], [1, 2 , 3], [1, 2 , 3]])

array = array.reshape(9, )
#or
array = array.reshape(-1)
print(array)