a = float(input("Nhập giá trị của a: "))
b = float(input("Nhập giá trị của b: "))
c = float(input("Nhập giá trị của c: "))


x = -b / (2 * a)


y = a * x**2 + b * x + c

print("Tọa độ của đỉnh là: (", round(x, 2), ",", round(y, 2), ")")
