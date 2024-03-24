# Nhập tọa độ của 3 đỉnh A, B, C của tam giác
xa = float(input("Nhập tọa độ x của điểm A: "))
ya = float(input("Nhập tọa độ y của điểm A: "))

xb = float(input("Nhập tọa độ x của điểm B: "))
yb = float(input("Nhập tọa độ y của điểm B: "))

xc = float(input("Nhập tọa độ x của điểm C: "))
yc = float(input("Nhập tọa độ y của điểm C: "))

#công thức
xg = (xa + xb + xc) / 3
yg = (ya + yb + yc) / 3

print("Tọa độ của trọng tâm là: (", round(xg, 2), ",", round(yg, 2), ")")
