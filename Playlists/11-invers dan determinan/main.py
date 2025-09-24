import numpy as np

a = np.array([
    [1,-1],
    [1,1]
])

print(a)

# invers matrix jika kita punya matrix a, maka inversnya a^-1
# jadi ketika matrix A.A^-1 = 1
# di matrix 1 itu begini [1,0],[0,1]
a_inv = np.linalg.inv(a)
print(a_inv)

# determinan matrix
det_a = np.linalg.det(a)
det_a_inv = np.linalg.det(a_inv)

print(det_a)
print(det_a_inv)

# kegunaannya untuk persamaan linear