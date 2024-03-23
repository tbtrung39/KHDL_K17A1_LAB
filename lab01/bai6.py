print("Nhập tọa độ của điểm A (x, y):")
x1 = float(input("x1: "))
y1 = float(input("y1: "))

print("Nhập tọa độ của điểm B (x, y):")
x2 = float(input("x2: "))
y2 = float(input("y2: "))

print("Nhập tọa độ của điểm C (x, y):")
x3 = float(input("x3: "))
y3 = float(input("y3: "))

x_trongtam = (x1 + x2 + x3) / 3
y_trongtam = (y1 + y2 + y3) / 3

print("Tọa độ của trọng tâm của tam giác là: (", round(x_trongtam, 2), ",", round(y_trongtam, 2), ")")
