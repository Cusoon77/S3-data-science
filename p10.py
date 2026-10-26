import numpy as np

nums = np.arange(16,dtype='int').reshape(-1,4)
print("original array:")
print(nums)
print("\nnew array after swapping first and last rows of the said array:")
nums = nums[[-1,1,2,0]]
print(nums)