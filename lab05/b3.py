a = int(input("Nhap so tu nhien la:"))
he_so = ''
if a == 0:
    print("So nhi phan la: 0")
else:
    while a > 0:
        he_so = str(a % 2) + he_so
        a //= 2
print("So nhi phan la:",he_so)