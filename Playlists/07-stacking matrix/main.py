import numpy as np

a = np.array([1,2,3])
b = np.array([3,4,5])

# stacking matrix, menumpuk matrix

c = np.hstack([a,b])
print(c)

d = np.vstack([a,b])
print(d)