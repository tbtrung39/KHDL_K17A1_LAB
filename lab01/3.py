import math
x1=float(input("nhap gia tri x1:"))
x2=float(input("Nhap gia tri x2:"))
print(f'Gia tri cua  vecto a  la:{x1,x2}')
y1=float(input("nhap gia tri y1:"))
y2=float(input("nhap gia tri cua y2:"))
print(f'Gia tri cuar vecto b la:{y1,y2}')
tich_vo_huong=math.sqrt(x1**2+x2**2)*math.sqrt(y1**2+y2**2)*((x1*y1+x2*y2)/math.sqrt(x1**2+x2**2)*math.sqrt(y1**2+y2**2))
print('Tich vo huong cua 2 vecto:',tich_vo_huong)