import numpy as np

a = np.array([
    [1,2,3],
    [4,5,6]
])

print(f'matrix a dengan ukuran: {a.shape}')
print(a)

# transpose matrix 
print('transpose matrix dari a: ')
print(a.transpose())
print(np.transpose(a))
print(a.T)

# flatten array, vector baris
print('flatten matrix a:')
print(a.ravel())
print(np.ravel(a))

# reshape matrix
print('reshape matrix a:')
print(a.reshape(3,2)) # ini sebenarnya di flatten dulu, baru diubah menjadi array sesuai urutan, 3 adalah kolom, 2 adalah baris

# resize matrix
print('resize matrix a:')
a.resize(3,2) # ini akan mengubah nilai a
print(a)