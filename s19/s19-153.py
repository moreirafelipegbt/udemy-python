import numpy as np

a = np.array([1,2,3,4,5,6,7,8])
boolean_array = [True, True, False, False, True, False, True, False]

result = a % 2 != 0

result2 = a[boolean_array]

print(a[result])

print(result2)