Ax, Ay = map(float, input("Nhập vector A, cách nhau bằng dấu cách: ").split())
Bx, By = map(float, input("Nhập vector B, cách nhau bằng dấu cách: ").split())
Cx, Cy = map(float, input("Nhập vector C, cách nhau bằng dấu cách: ").split())

Tx = (Ax + Bx + Cx) / 3
Ty = (Ay + By + Cy) / 3

print(f"Tọa độ trọng tâm của tam giác là: {Tx:.2f} {Ty:.2f}")