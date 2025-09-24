import numpy as np

A = np.array([
    [2,3],
    [1,2]
])
Y = np.array([
    [23],
    [14]
])
A_invers = np.linalg.inv(A)

X1 = np.dot(A_invers,Y)
X2 = np.linalg.solve(A,Y)

print(A)
print(Y)
print(X1)
print(X2)