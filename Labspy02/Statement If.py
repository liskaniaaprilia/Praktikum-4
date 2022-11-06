print('Liskania Aprilia 312210383')
print('Menampilkan bilangan terbesar dari 3 buah bilangan')
print('=====================================================')

a, b, c = (
  int(input('Masukkan nilai a: ')),
  int(input('Masukkan nilai b: ')),
  int(input('Masukkan nilai c: '))
)
if a > b and a > c:
  print('A yang terbesar')
elif b > a and b > c:
  print('B yang terbesar')
else:
  print('C yang terbesar')
