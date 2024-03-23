import math
a = float(input("Nhập hệ số a:"))
b = float(input("Nhập hệ số b:"))
c = float(input("Nhập hệ số c:"))
delta = b**2 - 4*a*c 
if a == 0:
    x = -c/b
    print("Phương trình có no duy nhất: ", x)
else:
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / 2*a
        x2 = (-b - math.sqrt(delta)) / 2*a
        print("Phương trình có 2 no phân biệt: ",x1,",",x2)
    elif delta == 0: 
        x0 = -b / 2*a
        print("Phương trình có 2 no kép: ", x0)
    else:
        print("Phương trình vô no")