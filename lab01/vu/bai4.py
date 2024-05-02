import math

x = float(input("Nhập giá trị của x: "))

numerator = -x + math.sqrt(x ** 2 + 4)
denominator = (x ** 4 + 17)** (1/7)

result = numerator / denominator
print("Giá trị của biểu thức là:", round(result, 2))
