# Operasi Aritmatika

a = 10
b = 3
'''OPERATOR SEDERHANA'''

# Operasi Tambah +
hasil = a + b
print(a, "+", b, "=", hasil)

# Operasi Pengurangan -
hasil = a - b
print(a, "-", b, "=", hasil)

# Operasi Perkalian *
hasil = a * b
print(a, "*", b, "=", hasil)

# Operasi Pembagian /
hasil = a / b
print(a, "/", b, "=", hasil)

# Operasi Eksponen (Pangkat) **
hasil = a ** b
print(a, "^", b, "=", hasil)

# Operasi Modulus (Sisa Pembagian) %
hasil = a % b
print(a, "%", b, "=", hasil)

# Operasi Floor Division //
# Pembulatan Kebawah
hasil = a // b
print(a, "//", b, "=", hasil)

'''PRIORITAS OPERASI, OPERATIONAL PRECEDENCE'''
x = 3
y = 2
z = 4
'''
Urutan Prioritas
1. () --> di dalam kurung
2. Exponen
3. Perkalian --> termasuk modulus dll
4. Pertambahan --> dan pengurangan
'''

hasil = x ** y * z + x / y - y % z // x

print(hasil)


