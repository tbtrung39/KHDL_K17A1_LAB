x = float(input("Nhập tọa độ x của điểm: "))
y = float(input("Nhập tọa độ y của điểm: "))
z = float(input("Nhập tọa độ z của điểm: "))
d_x_Oxy, d_y_Oxy, d_z_Oxy = x, y, -z
d_x_Oxz, d_y_Oxz, d_z_Oxz = x, -y, z
d_x_Oyz, d_y_Oyz, d_z_Oyz = -x, y, z
print("Tọa độ của điểm đối xứng qua mặt phẳng Oxy:", (d_x_Oxy, d_y_Oxy, d_z_Oxy))
print("Tọa độ của điểm đối xứng qua mặt phẳng Oxz:", (d_x_Oxz, d_y_Oxz, d_z_Oxz))
print("Tọa độ của điểm đối xứng qua mặt phẳng Oyz:", (d_x_Oyz, d_y_Oyz, d_z_Oyz))