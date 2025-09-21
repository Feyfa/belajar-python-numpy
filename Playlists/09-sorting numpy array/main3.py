import numpy as np

dtipe = [ ('nama', 'S10'),('tinggi',int) ]
data = [
    ('ucup',170),
    ('otong',160),
    ('marion',165),
]

a = np.array(data,dtype=dtipe)
print(a)

# sorting bedasarkan tinggi
print(np.sort(a,order='tinggi'))

# sorting bedasarkan nama
print(np.sort(a,order='nama'))