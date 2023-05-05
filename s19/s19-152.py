import numpy as np

a = np.array([[1,2,3], [7,8,9]])
b = np.array([[5,6,7], [10,11,12]])

result = np.vstack((a,b))
hresult = np.hstack((a, b))

print(result)

print(hresult)