import math
x1=float(input(" nhap gia tri x1: "))
x2=float(input("nhap gia tri x2: "))
print(f'gia tri cua vecto a la: {x1, x2}')
y1=float(input("nhap gia tri y1: "))
y2=float(input("nhap gia tri  y2: "))
print(f'gia tricua vecto b la: {y1, y2}')
tich_vo_huong=math.sqrt(x1**2+x2**2)*math.sqrt(y1**2+y2**2)*((x1*y1+x2*y2)/math.sqrt(y1**2+y2**2))
print("tich vo huong cua 2 vecto la: ", tich_vo_huong)