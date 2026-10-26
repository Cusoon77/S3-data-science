import numpy as np

x =  np.arange(21)
print("vectors")
print(x)

print("\nafter changing the sign of the numbers in the range from 9 to 15:")
x[(x>=9)&(x<=15)]=-1
print(x)
