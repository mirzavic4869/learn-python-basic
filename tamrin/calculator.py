# Calculator sederhana

angka_1 = float(input('masukkan angka pertama: '))
operator = input('masukkan operator (+ atau - atau * atau /): ')
angka_2 = float(input('masukkan angka kedua: '))


match operator:
    case '+':
        print(angka_1+angka_2)
    case '-':
        print(angka_1-angka_2)
    case '*':
        print(angka_1*angka_2)
    case '/':
        print(angka_1/angka_2)
    case _:
        print('anda memasukkan operator selain +,-,*,/')
