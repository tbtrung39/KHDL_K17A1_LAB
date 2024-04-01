x = float(input("Nhập vào tọa độ x: "))
y = float(input("Nhập vào tọa độ y: "))
z = float(input("Nhập vào tọa độ z: "))
toa_do_diem_doi_xung_xy = x, y, -z
toa_do_diem_doi_xung_xz = x, -y, z
toa_do_diem_doi_xung_yz = -x, y, z
print("Tọa độ của điểm đối xứng qua mặt phẳng Oxy:", toa_do_diem_doi_xung_xy)
print("Tọa độ của điểm đối xứng qua mặt phẳng Oxz:", toa_do_diem_doi_xung_xz)
print("Tọa độ của điểm đối xứng qua mặt phẳng Oyz:", toa_do_diem_doi_xung_yz)
