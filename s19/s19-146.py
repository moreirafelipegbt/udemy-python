import numpy as np

nums = np.array([[1,2,3,4],[4,5,6,7],[1,2,3,4]])

print(nums.shape)

for index, row in enumerate(nums):
    print(index, row)

for row in nums:
    for item in row:
        print(item)

encapsuled_nums = np.array([[[1,2,3]]])

print(encapsuled_nums.shape)