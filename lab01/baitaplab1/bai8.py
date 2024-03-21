print("Nhập tọa độ điểm A")
x_A = float(input("Nhập tọa độ điểm x_A:"))
y_A = float(input("Nhập tọa độ điểm y_B:"))
print("Nhập tọa độ điểm B")
x_B = float(input("Nhập tọa độ điểm x_B:"))
y_B = float(input("Nhập tọa độ điểm y_B:"))
print("Nhập tọa độ điểm C:")
x_C = float(input("Nhập tọa độ điểm x_C:"))
y_C = float(input("Nhập tọa độ điểm y_C:"))
x=(x_A+x_B+x_C)/3
y=(y_A+y_B+y_C)/3
print(f"Trọng tâm tam giác ABC là {x,y}")