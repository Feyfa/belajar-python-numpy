import numpy as np

# list python
a = [1,2,3,4,5]
b = [6,7,8,9,10]

# array numpy
anp = np.array([1,2,3,4,5])
bnp = np.array([6,7,8,9,10])

# ELEMENTWISE operation

# penjumlahan
penjumlahan1 = a + b # kalo menjumlahankan ke2 list python, maka 2 list tersebut akan di merge
penjumlahan2 = anp + bnp # kalo menjumlahkan array numpy, maka dia akan melakukan penjumlahan ELEMENTWISE operation
print(f'penjumlahan1 = {penjumlahan1}')
print(f'penjumlahan2 = {penjumlahan2}')

# pengurangan
# pengurangan = a - b # ini tidak bisa dijalankan, karena list dengan list tidak bisa dikurang
pengurangan1 = anp - bnp # kalo mengurangi array numpy, maka akan melakukan pengurangan ELEMENTWISE operation
print(f'pengurangan1 = {pengurangan1}')

# perkalian
perkalian1 = anp * bnp # # kalo mengalikan array numpy, maka akan melakukan perkalian ELEMENTWISE operation
print(f'perkalian1 = {perkalian1}')

# pembagian
pembagian1 = anp / bnp # # kalo membagi array numpy, maka akan melakukan pembagian ELEMENTWISE operation
print(f'pembagian1 = {pembagian1}')

# kuadrat
kuadrat1 = anp ** 2
print(f'kuadrat1 = {kuadrat1}')

# multidimensi array numpy
cnp = np.array([ [1,2,3],[3,4,5] ])
dnp = np.array([ [1,2,3],[3,4,5] ])

penjulahanMulti = cnp + dnp # ini penjumlahan ELEMENTWISE operation
perkalianMulti = cnp * dnp # ini perkalian ELEMENTWISE operation

print(f'penjulahanMulti = {penjulahanMulti}')
print(f'perkalianMulti = {perkalianMulti}')

