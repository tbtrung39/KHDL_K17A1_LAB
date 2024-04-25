import math


a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))


delta = b**2 - 4*a*c


if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("Phương trình có hai nghiệm:")
    print("x1 =", x1)
    print("x2 =", x2)
elif delta == 0:
    x = -b / (2*a)
    print("Phương trình có một nghiệm kép:")
    print("x =", x)
else:
    print("Phương trình không có nghiệm thực")