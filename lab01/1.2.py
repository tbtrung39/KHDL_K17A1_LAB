import math
x = float(input("Nhập giá trị của x: "))
F = (-x + math.sqrt(x**2 + 4)) / (math.sqrt(x**4 + 1))
print(f"f(x) = {F:.2f}")
