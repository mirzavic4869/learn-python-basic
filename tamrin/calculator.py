# Calculator sederhana

angka_1 = float(input('masukkan angka pertama: '))
operator = input('masukkan operator (+ atau - atau * atau /): ')
angka_2 = float(input('masukkan angka kedua: '))

if (operator == '+'):
    print(angka_1+angka_2)
elif (operator == '-'):
    print(angka_1-angka_2)
elif (operator == '*'):
    print(angka_1*angka_2)
elif (operator == '/'):
    print(angka_1/angka_2)
else:
    print('anda memasukkan operator selain +,-,*,/')
