import math
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))
x_vertex = -b / (2 * a)
y_vertex = a * x_vertex ** 2 + b * x_vertex + c
x = round(x_vertex, 2)
y = round(y_vertex, 2)
vertex =(x,y)
print("Đỉnh của phương trình bậc hai là:", vertex)