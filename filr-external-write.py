# mode write

with open('data_1.txt', 'w', encoding='utf-8') as file:
    file.write('Mirzam Avicena')

with open('data_1.txt', 'w', encoding='utf-8') as file:
    file.write('Hannah')  # overwrite


# mode append --> menimpa text
with open('data_2.txt', 'a', encoding='utf-8') as file:
    file.write('Hannah\n')

with open('data_2.txt', 'a', encoding='utf-8') as file:
    file.write('Ravi\n')

with open('data_2.txt', 'a', encoding='utf-8') as file:
    file.write('Umma\n')

# mode r+ --> menimpa isi text sesuai dengan panjang data
with open('data_3.txt', 'w', encoding='utf-8') as file:
    file.write('Umma-1\n')
    file.write('Umma-2\n')
    file.write('Umma-3\n')

with open('data_3.txt', 'r+', encoding='utf-8') as file:
    data = file.read()
    print(data)

with open('data_3.txt', 'r+', encoding='utf-8') as file:
    file.write('Ravi\n')
    file.write('Haura')
