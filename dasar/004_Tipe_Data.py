# a = 10, a adalah variabel dengan nilai 10

# Tipe Data: Angka Satuan Tdk Berkoma (Integer)
data_integer = 1
#print(type(data_integer))
#print("data : ", data_integer, ", bertipe : ", type(data_integer))
print("Data: ", data_integer)
print(" - Bertipe : ", type(data_integer))

# TIPE DATA: Angka dengan koma (Float) / TDK ADA Double
data_float = 1.5
print("Data : ", data_float)
print(" - Bertipe : ", type(data_float))

# TIPE DATA: Kumpulan Karakter (String)
data_string = "Ucup"
print("Data : ", data_string)
print(" - Bertipe : ", type(data_string))

# TIPE DATA: Biner True False (Boolean)
data_bool = True
print("Data : ", data_bool)
print(" - Bertipe : ", type(data_bool))

# TIPE DATA KHUSUS: Bilangan Kompleks
data_complex = complex(5, 6)
print("Data : ", data_complex)
print(" - Bertipe : ", type(data_complex))

# TIPE DATA KHUSUS: Tipe Data Dari Bahasa C
from ctypes import c_double

data_c_double = c_double(10.5)
print("Data : ", data_c_double)
print(" - Bertipe : ", type(data_c_double))
