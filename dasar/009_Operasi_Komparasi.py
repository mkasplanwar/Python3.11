""" OPERASI KOMPARASI

--> Setiap hasil dari operasi komparasi adalah boolean

    >, <, >=, <=, ==, !=, is , is not

    KOMPARATIF --> <, >, >=, <=, ==, !=
    --> dapat bekerja pada syntax literal
    A == 4
    A --> Ada nilainya --> Memakan Memori
    4 --> Literal --> Tdk memakan materi

IS, IS NOT --> membandingkan memori / object

"""
a = 4
b = 2

# Lebih Besar dari >
print("======== Lebih Besar Dari > ========")
hasil = a > 3
print(a,">",3,"=",hasil)
hasil = b > 3
print(b,">",3,"=",hasil)
hasil = b > 2
print(b,">",2,"=",hasil)

# kurang Dari <
print("======== Kurang Dari < ========")
hasil = a < 3
print(a,"<",3,"=",hasil)
hasil = b < 3
print(b,"<",3,"=",hasil)
hasil = b < 2
print(b,"<",2,"=",hasil)

# Lebih Dari Sama Dengan >=
print("======== Lebih Dari Sama Dengan >= ========")
hasil = a >= 3
print(a,">=",3,"=",hasil)
hasil = b >= 3
print(b,">=",3,"=",hasil)
hasil = b >= 2
print(b,">=",2,"=",hasil)

# Kurang Dari Sama Dengan <=
print("======== Kurang Dari Sama Dengan <= ========")
hasil = a <= 3
print(a,"<=",3,"=",hasil)
hasil = b <= 3
print(b,"<=",3,"=",hasil)
hasil = b <= 2
print(b,"<=",2,"=",hasil)

# Sama Dengan ==
print("======== Sama Dengan == ========")
hasil = a == 4
print(a,"==",4,"=",hasil)
hasil = b == 3
print(b,"==",3,"=",hasil)
hasil = b == 2
print(b,"==",2,"=",hasil)
# '=' Assignment, '==' Komparasi

# Tidak Sama Dengan !=
print("======== Tidak Sama Dengan != ========")
hasil = a != 4
print(a,"!=",4,"=",hasil)
hasil = b != 3
print(b,"!=",3,"=",hasil)
hasil = b != 2
print(b,"!=",2,"=",hasil)

# 'IS' sebagai komparasi obejct identity
print("======== Object Identity (IS) ========")
x = 5 # ini adalah assignment membuat obejct
y = 5

print("Nilai x = ", x, "Id = ", hex(id(x)))
print("Nilai y = ", y, "Id = ", hex(id(y)))

hasil = x is y
print("x is y = ", hasil)

# 'IS NOT' sebagai komparasi obejct identity
print("======== Object Identity (IS NOT) ========")
x = 5 # ini adalah assignment membuat obejct
y = 6

print("Nilai x = ", x, "Id = ", hex(id(x)))
print("Nilai y = ", y, "Id = ", hex(id(y)))

hasil = x is not y
print("x is not"
      " y = ", hasil)