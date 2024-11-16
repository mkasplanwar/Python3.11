# Mengambil input dari user

# DATA YANG DI MASUKKAN PASTI STRING
data = input("Masukkan Data : ")

print("Data : ", data)
print("Tipe Data: ", type(data))

# jika kita ingin mengambil data INTEGER, maka
angka = float (input("Masukkan Angka : "))
print("Data : ", angka)
print("Tipe Data: ", type(angka))

# Bagaimana dengan Boolean
biner = bool(int(input("Masukkan Nilai Boolean : ")))

print("Data : ", biner)
print("Tipe Data: ", type(biner))