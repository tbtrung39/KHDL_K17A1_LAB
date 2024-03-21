import math
x = int(input("Nhập vào giá trị x:"))
f = (-x + math.sqrt(x**2+4))/math.sqrt(x**4+1)
print("Giá trị của biểu thức là:",round(f, 2))