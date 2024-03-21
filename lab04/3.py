import math

x = float(input("Nhập giá trị x: "))
n = 2  # Bắt đầu với n = 2
a = 1e-4 # với e là giá trị 2,71

b = 1.0
c = -1
d = 1

while True:
    d = d * x * x / (n * (n - 1))
    g = d * c
    b += g
    n += 2
    c*= -1
    if abs(g) < a:
        break

gia_tri = b
bien_x = math.cos(x)
print(f"Giá trị xấp xỉ của cos({x}) với sai số 10^(-4) là: {gia_tri}")
