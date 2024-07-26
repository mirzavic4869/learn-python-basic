print(3*"=", 'Membaca file external dengan open', 3*'=')

file = open('data.txt', mode='r')
# membaca file keseluruhan
print(file.read())
# membaca per baris
print(file.readline(), end='')

print(file.readable())


print(3*"=", 'Membaca file external dengan with', 3*'=')

with open('data.txt', mode='r') as file:
    content = file.readline()
    print(content, end='')
    print(f'apakah file sudah diclose {file.closed}')

print(f'apakah file sudah diclose {file.closed}')
