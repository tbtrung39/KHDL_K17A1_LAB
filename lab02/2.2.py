a = float(input("Nhap he so a: "))
b = float(input("Nhap he so b: "))
c = float(input("Nhap he so c: "))
deta = b**2 - 4*a*c
if deta > 0:
    x1 = (-b + deta**0.5) / (2*a)
    x2 = (-b - deta**0.5) / (2*a)
    print("Phuong trinh co 2 ngiem phan biet: ", "x1 = ", x1 , "x2 = ", x2)
elif deta == 0:
    x = -b / (2*a)
    print("phuong trinh co nghiem kep: ", "x = ", x)
else:
    print("Phuong trinh khong co nghiem thuc: ")