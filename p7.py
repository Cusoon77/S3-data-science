import numpy as np

x = np.array([[1,0],[0,1]])

print ("array")
print(x)

print("\n sum of al elements")
print(np.sum(x))
print("\n sum of each column:")
print(np.sum(x, axis=0))
print("\n sum of each row")
print(np.sum(x, axis=1))

