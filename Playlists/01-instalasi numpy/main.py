import numpy as np

a = np.array([1,2,3,4,5])
b = [1,2,3,4,5]

print(a)
print(b)

a = a + 1 #kalo pakai array dari numpy itu bisa melakukan penambaha seperti ini, tiap komponen akan di tambahkan 1

# b = b + 1 #kalo pakai list bawaan python tidak bisa begini
b = b + [1] #harus dijumlahkan dengan list

print(a)
print(b)