a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

deta = b**2 - 4*a*c

if deta > 0:
    x1 = (-b + deta**0.5) / (2*a)
    x2 = (-b - deta**0.5) / (2*a)
    print("Phương trình có 2 nghiệm phân biệt:")
    print("x1 =", x1)
    print("x2 =", x2)
elif deta == 0:
    x = -b / (2*a)
    print("Phương trình có nghiệm kép:")
    print("x =", x)
else:
    print("Phương trình không có nghiệm thực")