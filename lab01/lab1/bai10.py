import math

x = float(input("Nhập giá trị của x: "))

f = math.log(x, 4) + math.log(x**2)

print("Giá trị của biểu thức là:", round(f, 2))
