import math
x = float(input("Nhập giá trị x : "))
saiso = 1e-4
n = 2
cos_x = 1
ct = 1
while abs(ct) >= saiso:
    ct *= -(x ** 2) / (n * (n - 1))
    cos_x += ct
    n += 2
print("Giá trị gần đúng của cos({}) là: {}".format(x, cos_x))