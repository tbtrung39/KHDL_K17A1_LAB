x = float(input("Nhập tọa độ x của điểm: "))
y = float(input("Nhập tọa độ y của điểm: "))
z = float(input("Nhập tọa độ z của điểm: "))

# Tính tọa độ của điểm đối xứng qua mặt phẳng Oxy,Oxz, Oyz
diem_doi_xung_oxy = (x, y, -z)
diem_doi_xung_oxz = (x, -y, z)
diem_doi_xung_oyz = (-x, y, z)

# In kết quả
print("Tọa độ điểm đối xứng qua mặt phẳng Oxy là:", diem_doi_xung_oxy)
print("Tọa độ điểm đối xứng qua mặt phẳng Oxz là:", diem_doi_xung_oxz)
print("Tọa độ điểm đối xứng qua mặt phẳng Oyz là:", diem_doi_xung_oyz)

