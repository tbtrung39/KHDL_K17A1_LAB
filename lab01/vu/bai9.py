
x = float(input("Nhập tọa độ x của điểm: "))
y = float(input("Nhập tọa độ y của điểm: "))
z = float(input("Nhập tọa độ z của điểm: "))

#  mặt phẳng Oxy
x_xy = x
y_xy = y
z_xy = -z

# Tính tọa độ của điểm đối xứng qua mặt phẳng Oxz
x_xz = x
y_xz = -y
z_xz = z

# Tính tọa độ của điểm đối xứng qua mặt phẳng Oyz
x_yz = -x
y_yz = y
z_yz = z

# In kết quả
print("Tọa độ của điểm đối xứng qua mặt phẳng Oxy:", (x_xy, y_xy, z_xy))
print("Tọa độ của điểm đối xứng qua mặt phẳng Oxz:", (x_xz, y_xz, z_xz))
print("Tọa độ của điểm đối xứng qua mặt phẳng Oyz:", (x_yz, y_yz, z_yz))
