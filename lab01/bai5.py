import math

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

x_dinh = -b / (2 * a)
y_dinh = a * x_dinh**2 + b * x_dinh + c

print("Đỉnh của phương trình bậc hai là: (", round(x_dinh, 2), ",", round(y_dinh, 2), ")")
