# Latihan Konversi Perhitungan Suhu

print("PROGRAM KONVERSI SUHU SEDERHANA")

celcius = float(input('Maukkan suhu dalam celcius'))
print('Suhu dalam celcius adalah', celcius, 'Celcius')

# Reamur
reamur = (4/5)*celcius
print('Suhu dalam reamur adalah', reamur, 'Reamur')

# Fahrenheit
fahrenheit = ((9/5)*celcius) + 32
print('Suhu dalam fahrenheit adalah', fahrenheit, 'Fahrenheit')

# Kelvin
kelvin = celcius+273
print('Suhu dalam kelvin adalah', kelvin, 'Kelvin')


print("==============")

reamur = float(input("masukkan suhu dalam reamur"))
print('Suhu dalam reamur adalah', reamur, 'Reamur')

# celcius
celcius = (5/4)*reamur
print('Suhu dalam celcius adalah', celcius, 'Celcius')

# Fahrenheit
fahrenheit = ((9/4)*reamur) + 32
print('Suhu dalam fahrenheit adalah', fahrenheit, 'Fahrenheit')

# Kelvin
kelvin = ((5/4)*reamur)+273
print('Suhu dalam kelvin adalah', kelvin, 'Kelvin')

print("==============")

fahrenheit = float(input("masukkan suhu dalam fahrenheit"))
print('Suhu dalam fahrenheit adalah', fahrenheit, 'Fahrenheit')

# celcius
celcius = (5/9)*(fahrenheit-32)
print('Suhu dalam celcius adalah', celcius, 'Celcius')

# reamur
reamur = (4/9)*(fahrenheit-32)
print('Suhu dalam reamur adalah', reamur, 'Reamur')

# Kelvin
kelvin = ((5/9)*(fahrenheit-32))+273
print('Suhu dalam kelvin adalah', kelvin, 'Kelvin')

print("==============")

kelvin = float(input("masukkan suhu dalam kelvin"))
print('Suhu dalam kelvin adalah', kelvin, 'Kelvin')

# celcius
celcius = kelvin-273
print('Suhu dalam celcius adalah', celcius, 'Celcius')

# reamur
reamur = (4/5)*(kelvin-273)
print('Suhu dalam reamur adalah', reamur, 'Reamur')

# fahrenheit
fahrenheit = ((9/5)*(kelvin-273))+32
print('Suhu dalam fahrenheit adalah', fahrenheit, 'Fahrenheit')
