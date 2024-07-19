# folder _pycache_ berisi file compiler yang membuat eksekusi kode semakin cepat


import package_sederhana
import package_sederhana.matematika
import sains.matematika
from sains import fisika
import time

t_start = time.time()

hasil_tambah = sains.matematika.tambah(1, 2, 3, 4, 5)
print(f'hasil_tambah adalah = {hasil_tambah}')
t_end = time.time()

print(t_end-t_start)

gaya = fisika.gaya(2, 4)
print(f'gaya sebesar = {gaya}')

hasil_kali = package_sederhana.matematika.kali(1, 2, 3)
print(f'hasil kali adalah = {hasil_kali}')
