# Operasi Logika atau Boolean
print('===== OR =====')

# OR (jika salah satu True maka True)
a = True
b = False
print(a or b)
print(a or a)
print(b or b)
print(b or a)

print('===== AND =====')

# AND (jika salah satu False maka False)
a = True
b = False
print(a and b)
print(a and a)
print(b and b)
print(b and a)

print('===== XOR =====')

# XOR (jika 2 nilai berbeda maka False)
a = True
b = False
print(a ^ b)
print(a ^ a)
print(b ^ b)
print(b ^ a)

print('===== NOT =====')

# NOT (kebalikan nilai)
a = True
b = not a
print(b)
