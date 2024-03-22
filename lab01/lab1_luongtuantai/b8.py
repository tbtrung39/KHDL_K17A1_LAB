x= float(input("nhập tọa độ điểm x: "))
y= float(input("nhập tọa độ điểm y: "))
z= float(input("nhập tọa độ điểm z: "))
# Tính tọa độ của điểm đối xứng qua mặt phẳng Oxy
x_doi_xung_Oxy = x
y_doi_xung_Oxy = y
z_doi_xung_Oxy = -z

# Tính tọa độ của điểm đối xứng qua mặt phẳng Oxz
x_doi_xung_Oxz = x
y_doi_xung_Oxz = -y
z_doi_xung_Oxz = z

# Tính tọa độ của điểm đối xứng qua mặt phẳng Oyz
x_doi_xung_Oyz = -x
y_doi_xung_Oyz = y
z_doi_xung_Oyz = z

print("Tọa độ của điểm đối xứng qua mặt phẳng Oxy là: ({}, {}, {})".format(x_doi_xung_Oxy, y_doi_xung_Oxy, z_doi_xung_Oxy))
print("Tọa độ của điểm đối xứng qua mặt phẳng Oxz là: ({}, {}, {})".format(x_doi_xung_Oxz, y_doi_xung_Oxz, z_doi_xung_Oxz))
print("Tọa độ của điểm đối xứng qua mặt phẳng Oyz là: ({}, {}, {})".format(x_doi_xung_Oyz, y_doi_xung_Oyz, z_doi_xung_Oyz))