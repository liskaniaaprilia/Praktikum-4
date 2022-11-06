print('Perulangan #Latihan 1')
print('Liskania Aprilia')
print('312210383')
print('==========================')

for i in range(10):
    for b in range(10):
        if i + b < 10:
            jarak = "  "
        else :
            if i + b < 20:
                jarak = " "
        print(i+b, end=jarak)
    print()