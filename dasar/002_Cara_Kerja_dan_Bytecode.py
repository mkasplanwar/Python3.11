'''
Python --> Bahasa Pemprograman --> Interpreted

Source Code (Main Py) --> (Interpreter) Python 3.11 --> Terminal/Dijalankan

baris pertama --> Penerjemah (Interpreter) --> terminal
baris kedua

Source Code --> C++ (Compiled) --> Excutable (.exe) terminal

jadi python tidak perlu di compile, jadi langsung bisa 
di run di terminal
'''
import time
start_time = time.time()

print ("Hello World")
print ("Hello")
print ("World")

# ini adalah comment

a = 10 #ini adalah comment
"""multi line commen
ini ada lah comment multi line """
 
print(a)

print (time.time() - start_time, "Detik")

#Kita Bisa mengcompile python ke yang namanya bytecode

'''
Source Code (Syntax) --> Interpreted --> Tampilkan

                    --> compile --> Bytecode
Membuka File Python Di Terminal:
            --> python namafile.py
Mengubah File Interpreted Menjadi .exe:
    --> python -m_compile namafile.py
Membuka File .exe:
    --> cd __pycache__
Mengcompile .exe:
        --> python Main.cpython-38.pyc
    
'''
