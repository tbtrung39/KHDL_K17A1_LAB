#Viết chương trình nhập vào một tọa độ trong không gian Oxyz. Tính tọa độ của điểm đối xứng với nó qua mặt phẳng Oxy, Oxz, Oyz
x = float(input("Nhập tọa độ x của điểm: "))
y = float(input("Nhập tọa độ y của điểm: "))
z = float(input("Nhập tọa độ z của điểm: "))
# Tính tọa độ của điểm đối xứng qua mặt phẳng Oxy
doi_xung_Oxy = (x, y, -z)
# Tính tọa độ của điểm đối xứng qua mặt phẳng Oxz
doi_xung_Oxz = (x, -y, z)
# Tính tọa độ của điểm đối xứng qua mặt phẳng Oyz
doi_xung_Oyz = (-x, y, z)
print("Tọa độ của điểm đối xứng qua mặt phẳng Oxy là:", doi_xung_Oxy)
print("Tọa độ của điểm đối xứng qua mặt phẳng Oxz là:", doi_xung_Oxz)
print("Tọa độ của điểm đối xứng qua mặt phẳng Oyz là:", doi_xung_Oyz)
