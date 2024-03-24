import math
x = float(input("Nhập giá trị của x: "))

a = math.log(x, 4) + math.log(x**2)
a_rounded = round(a, 2)
print("Giá trị của biểu thức là:", a_rounded)
