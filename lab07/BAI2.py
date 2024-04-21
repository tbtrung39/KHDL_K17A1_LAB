num = []
while True:
    a = input('Nhap mot so tu nhien(an ENTER de ket thuc): ')
    if a == '':
        break
    if a.isdigit():
        num.append(int(a))
A = set(num)
print('Tap hop A la: ',A)