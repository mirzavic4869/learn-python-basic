# import matematika as math


# hasil_tambah = tambah(1, 2, 3, 4)
# print(f'hasil_tambah = {hasil_tambah}')

# hasil_kali = math.kali(1, 2, 3, 4)
# print(f'hasil_kali = {hasil_kali}')

# hasil_pangkat2 = math.pangkat(2)
# print(f'hasil_pangkat2 = {hasil_pangkat2(2)}')

from matematika import tambah as plus, kali as multi
from matematika import *


hasil_tambah = plus(1, 2, 3, 4)
print(f'hasil_tambah = {hasil_tambah}')

hasil_kali = multi(1, 2, 3, 4)
print(f'hasil_kali = {hasil_kali}')

hasil_pangkat2 = pangkat(2)
print(f'hasil_pangkat2 = {hasil_pangkat2(2)}')
