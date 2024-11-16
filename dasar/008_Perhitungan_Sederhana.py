""" LATIHAN KONVERSI SATUAN TEMPERATURE """

# program konversi celcius ke satuan lain

print("PROGRAM KONVERSI TEMPERATURE")

celcius = float(input("Masukkan suhu dalam celcius: "))
print("Suhu adalah ", celcius, "Celcius")

# Reamur
reamur = (4 / 5) * celcius
print("Suhu dalam reamur adalah ", reamur, "Reamur")

# Fahreinheit
fahreinhet = ((9/5) * celcius) + 32
print("Suhu dalam fahreinhet adalah ", fahreinhet, "fahreinhet")

# Kelvin
kelvin = celcius + 273.5
print("Suhu dalam kelvin adalah ", kelvin, "kelvin")

