# tebak angka

from random import randint

angka = randint(1, 10)

life = 3

while 0 < life:
    tebak_angka = int(input('masukan angka 1-10: '))

    print('='*10)

    if (tebak_angka < 1 or tebak_angka > 10):
        print('anda tidak memasukkan angka 1-10')
    else:
        if (tebak_angka < angka):
            print('salah, angka yang anda masukkan lebih kecil')
        elif (tebak_angka > angka):
            print('salah, angka yang anda masukkan lebih besar')
        elif (tebak_angka == angka):
            print('Selamat anda benar')
            break

    life -= 1
    if (life == 0):
        print('nyawa anda habis')
        break
