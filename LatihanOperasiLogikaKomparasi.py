# Latihan Operasi Logika dan Komparasi

# 1. -----0++++5----8++++11-------
# 2. +++++0-----5++++8-------11+++++

angka = float(input(
    "masukkan angka lebih dari 0 dan kurang dari 5 \n atau lebih dari \n 8 dan kurang dari 11"))

isLebihDari = angka > 0
print(isLebihDari)

isKurangDari = angka < 5
print(isKurangDari)

isLebihDari2 = angka > 8
print(isLebihDari2)

isKurangDari2 = angka < 11
print(isKurangDari2)

print(10*"=")

isCorrect = ((isLebihDari and isKurangDari)
             or (isKurangDari2 and isLebihDari2))

print(isCorrect)

print(10*"=")

angka = float(input(
    "masukkan angka kurang dari 0 atau lebih dari 5 \n dan kurang dari \n 8 atau lebih dari 11"))

isKurangDari = angka < 0
print(isKurangDari)

isLebihDari = angka > 5
print(isLebihDari)

isKurangDari2 = angka < 8
print(isKurangDari2)

isLebihDari2 = angka > 11
print(isLebihDari2)

print(10*"=")

isCorrect = ((isKurangDari or isLebihDari)
             and (isKurangDari2 or isLebihDari2))

print(isCorrect)
