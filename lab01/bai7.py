x = float(input("Nhập tọa độ x của điểm: "))
y = float(input("Nhập tọa độ y của điểm: "))
z = float(input("Nhập tọa độ z của điểm: "))

# Tính tọa độ của điểm đối xứng qua mặt phẳng Oxy
x_doi_xung_oxy = x
y_doi_xung_oxy = y
z_doi_xung_oxy = -z

# Tính tọa độ của điểm đối xứng qua mặt phẳng Oxz
x_doi_xung_oxz = x
y_doi_xung_oxz = -y
z_doi_xung_oxz = z

# Tính tọa độ của điểm đối xứng qua mặt phẳng Oyz
x_doi_xung_oyz = -x
y_doi_xung_oyz = y
z_doi_xung_oyz = z

print("Tọa độ của điểm đối xứng qua mặt phẳng Oxy là: (", x_doi_xung_oxy, ",", y_doi_xung_oxy, ",", z_doi_xung_oxy, ")")
print("Tọa độ của điểm đối xứng qua mặt phẳng Oxz là: (", x_doi_xung_oxz, ",", y_doi_xung_oxz, ",", z_doi_xung_oxz, ")")
print("Tọa độ của điểm đối xứng qua mặt phẳng Oyz là: (", x_doi_xung_oyz, ",", y_doi_xung_oyz, ",", z_doi_xung_oyz, ")")
