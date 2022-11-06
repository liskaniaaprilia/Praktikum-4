print("Latihan 2 - Menampilkan Bilangan Terbesar")
print("Liskania Aprilia 312210383")
print("=========================================")

max = 0 # Menentukan bilangan terbesar
while True :
    a = int(input("Masukkan bilangan = "))
    if max < a:
        max = a
    if a== 0:
       break # Mengakhiri perulangan

print ("Bilangan Terbesar adalah" ,max)


