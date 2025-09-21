import numpy as np

a = np.floor(np.random.randn(1,6) * 10)

print(a)

print(f'nilai max dari a = {a.max()}')
print(f'index dari nilai max a = {a.argmax()}')

print(f'nilai min dari a = {a.min()}')
print(f'index dari nilai min a = {a.argmin()}')

print(f'mengurutkan nilai dari a')
print(np.sort(a)) # ini mengurutkan value nya secara asc
print(np.argsort(a)) # ini mengurutkan value nya secara asc, dan mengambil index nya