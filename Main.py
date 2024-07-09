from ctypes import c_double
print("Hello World")
a = 10+2
print(a)
# ini comment
"""ini comment
tentu saja

"""

# Variabel adalah tempat menyimpan data

# menaruh data /assigment
a = 10
b = 2
lebar = 200

# penamaan
nilai_a = 2  # underscore boleh, kebab tidak boleh
nilaiItem = 7  # boleh
juta20 = 20000000  # angka tidak boleh di depan

print('Nilai a =', lebar)

# Tipe Data

data_integer = 10
print('data:', data_integer)
print('type:', type(data_integer))

data_float = 10.5
print('data:', data_float)
print('type:', type(data_float))

data_string = "10"
print('data:', data_string)
print('type:', type(data_string))

data_bool = True
print('data:', data_bool)
print('type:', type(data_bool))


data_c_double = c_double(10.5)
print('data:', data_c_double)
print('type:', type(data_c_double))


def genapGanjil(num):
    arr = []
    for x in range(num):
        if (x % 2 == 0):
            arr.append(f'{x} adalah bilangan genap')
        else:
            arr.append(f'{x} adalah bilangan ganjil')

    return arr


print(genapGanjil(5))
