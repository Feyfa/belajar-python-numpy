import numpy as np

# membuat matrix dengan tipe data tertentu
a = np.array([
    [1,2,3],
    [3,4,5]
], dtype=float)

print(a)





# membuat matrix dengan menggunakan function
def kuadrat(baris,kolom):
    return kolom ** 2

def jumlah(baris,kolom):
    return kolom + baris

# np.fromfunction(function,ukuran matrix,tipe)
# np.fromfunction(function,(jumlah baris,jumlah kolom),tipe)
b = np.fromfunction(kuadrat,(1,10),dtype=int)
c = np.fromfunction(jumlah,(4,4),dtype=float)
e = np.fromfunction(
    lambda baris,kolom: baris + kolom, 
    (1,10), 
    dtype=int
)

print(b)
print(c)
print(e)





# membuat array atau matrix dengan menggunakan iterable
iterable = (x**x for x in range(5))
h = np.fromiter(iterable,dtype=int)

print(h)





# multitype array
# nama untuk kolom 1, tinggi untuk kolom 2, tipe data list dan tiap element nya tuple
dtipe = [ ('nama','S255'),('tinggi', int) ]
# tipe data list dan tiap element nya tuple
data = [
    ('ucup', 150),
    ('otong', 160),
    ('mario', 180)
]
i = np.array(data, dtype=dtipe)

print(i)