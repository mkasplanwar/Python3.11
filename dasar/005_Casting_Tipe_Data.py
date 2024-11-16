# CASTING: merubah dari satu tipe data ke tipe data yang lain

# TIPE DATA: int, float, str, bool

## INTEGER
print("=====INTEGER=====")
data_int = 9
print("data = ", data_int, ", type = ", type(data_int))

data_float = float(data_int)
data_string = str(data_int)
data_bool = bool(data_int) # Akan false jika 0
print("data = ", data_float, ", type = ", type(data_float))
print("data = ", data_string, ", type = ", type(data_string))
print("data = ", data_bool, ", type = ", type(data_bool))

## FLOAT
print("=====FLOAT=====")
data_float = 9.5
print("data = ", data_int, ", type = ", type(data_int))

data_int = int(data_float) # Akan dibulatkan ke BAWAH
data_string = str(data_float)
data_bool = bool(data_float) # Akan false jika 0
print("data = ", data_int, ", type = ", type(data_int))
print("data = ", data_string, ", type = ", type(data_string))
print("data = ", data_bool, ", type = ", type(data_bool))

## BOOLEAN
print("=====BOOLEAN=====")
data_bool = True
print("data = ", data_bool, ", type = ", type(data_bool))

data_int = int(data_bool)
data_string = str(data_bool)
data_float = float(data_bool)
print("data = ", data_int, ", type = ", type(data_int))
print("data = ", data_string, ", type = ", type(data_string))
print("data = ", data_float, ", type = ", type(data_float))

## STRING
print("=====STRING=====")
data_str = "10"
print("data = ", data_str, ", type = ", type(data_str))
# int (data_str) --> string harus angka
# float (data_str) --> string harus angka
data_int = int(data_str)  # teks tdk bisa di ubah menjadi angka
data_string = bool(data_str) # false jika string kosong
data_float = float(data_str) # teks tdk bisa di ubah menjadi angka
print("data = ", data_int, ", type = ", type(data_int))
print("data = ", data_bool, ", type = ", type(data_bool))
print("data = ", data_float, ", type = ", type(data_float))


