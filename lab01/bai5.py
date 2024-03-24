import math
a = float(input("Nhập hệ số a của phương trình bậc hai: "))
b = float(input("Nhập hệ số b của phương trình bậc hai: "))
c = float(input("Nhập hệ số c của phương trình bậc hai: "))
x = -b / (2 * a)
y = a * x ** 2 + b * x + c
print("Đỉnh là: (", round(x, 2), ",", round(y, 2), ")")