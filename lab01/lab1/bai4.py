import math

x = float(input("Nhập giá trị của x: "))

tu_so = -x + math.sqrt(x ** 2 + 4)
mau_so = (x ** 4 + 17)** (1/7)

f = tu_so / mau_so

print("Giá trị của biểu thức là:", round(f, 2))
