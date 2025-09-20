import numpy as np

# membuat vector 
a = np.array([1,2,3,4,5])
b = np.array([1.5,2.5,5,6,7])
print(f'a = {a}')
print(f'b = {b}')

# membuat vector dengan range np.arange(batas bawah,batas atas,lompat)
c = np.arange(1,10,2)
print(f'c = {c}')

# membuat linear space
# membuat range 4 komponen dengan jarak yang sama, dimulai dari 1 - 10
# sekarangg, bagaimana ini bekerja
# rasio = (batas atas - batas bawah) / (space - 1)
# rasio = (10 - 1) / (4 - 1)
# rasio = 9 / 3 = 3
# nah polanya jadi 
# [ 1  4(1+3)  7(4+3)  10(7+3) ]
d = np.linspace(1,10,4)
print(f'd = {d}')

# array multidimensi / matrix
e = np.array([ (1,2,3),(4,5,6) ])
print(f'e = {e}')

# matrix dengan nilai nol
f = np.zeros(5) # ini untuk vector atau array 1 dimensi
g = np.zeros((5,5)) # ini untuk matrix atau array 2 dimensi
print(f'f = {f}')
print(f'g = {g}')

# matrix dengan nilai satu
h = np.ones((5,5))
print(f'h = {h}')

# matrix identitas
"""
akan membuat hasil seperti ini, 5 itu ada width dan heigh dari matrix tersebut
[
    [1. 0. 0. 0. 0.]
    [0. 1. 0. 0. 0.]
    [0. 0. 1. 0. 0.]
    [0. 0. 0. 1. 0.]
    [0. 0. 0. 0. 1.]
]
"""
i1 = np.identity(5) # ini matrix yang width dan heigh nya sama
i2 = np.eye(5, 10) # ini matrix yang width dan heigh nya bisa beda
print(f'i1 = {i1}')
print(f'i2 = {i2}')