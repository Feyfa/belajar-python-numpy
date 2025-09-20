import numpy as np

a = np.array([ 
    [1,2],
    [3,4] 
])
b = np.array([
    [1,1],
    [1,1]
])

print('matrix a: ')
print(a)

print('matrix b: ')
print(b)

# perkalian matrix
"""
1,2    1,1
3,4    1,1
-----------
3,3
7,7
"""
c1 = np.dot(a,b)
c2 = a.dot(b)
c3 = a @ b

print('matrix c1: ')
print(c1)

print('matrix c2: ')
print(c2)

print('matrix c3: ')
print(c3)

# contoh lain
x = np.array([
    [1,2,3],
    [4,5,6],
])
y = np.array([
    [7,8,9],
    [10,11,12],
])
yT = y.T # transpose matrix

# z = x.dot(y) # ini tidak bisa dilakukan karena matrix tidak bisa jika (2x3) dikali dengan matrix (2x3), makanya y harus di transpose teerlebih dahulu supaya (2x3) dikali (3x2)
z = x.dot(yT)

print(z)