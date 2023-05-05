import numpy as np

nums = np.array([1,2,3,4,5,6,7,8,9,10])

print(nums[:])

print(nums[::1])

print(nums[::2])

print(nums[0:7:2]) #When from the left to right, the 7 (or second ":" is exclusive, or -1)

print(nums[7:0:-1]) #When from the righ to left, the 8 (or +1 is inclusive)

print(nums[7:0:-2])

#Print the array inverse
print(nums[::-1])