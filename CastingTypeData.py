# Casting tipe data adalah mengkonversi tipe data
# merubah dari ttipe data satu ke yang lain

data_int = 7
print('data:', data_int, 'type:', type(data_int))

# Integer
data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)  # akan false jika int = 0
print('data:', data_float, 'type:', type(data_float))
print('data:', data_str, 'type:', type(data_str))
print('data:', data_bool, 'type:', type(data_bool))
print("====")

# Float
data_float = 7.9

data_int = int(data_float)  # Pembulatan ke bawah
data_str = str(data_float)
data_bool = bool(data_float)  # akan false jika int = 0
print('data:', data_int, 'type:', type(data_int))
print('data:', data_str, 'type:', type(data_str))
print('data:', data_bool, 'type:', type(data_bool))
print("====")

# String

data_string = "0"

data_int = int(data_string)  # Pembulatan ke bawah
data_float = float(data_string)
data_bool = bool(data_string)  # akan false jika str = ''
print('data:', data_int, 'type:', type(data_int))
print('data:', data_float, 'type:', type(data_float))
print('data:', data_bool, 'type:', type(data_bool))
print("====")

# Boolean

data_bool = True

data_int = int(data_bool)  # Pembulatan ke bawah
data_float = float(data_bool)
data_str = str(data_bool)  # akan false jika int = 0
print('data:', data_int, 'type:', type(data_int))
print('data:', data_float, 'type:', type(data_float))
print('data:', data_str, 'type:', type(data_str))
print("====")
