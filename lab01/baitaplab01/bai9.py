x = float(input("Nhập x:"))
y = float(input("Nhập y:"))
z = float(input("Nhập z:"))
#đối xứng qua oxy
x_doi_xung = -x
y_doi_xung = y
z_doi_xung = z
#đối xứng qua oxz
x_doi_xung1 = x
y_doi_xung1 = -y
z_doi_xung1 = z
#đối xứng qua oyz
x_doi_xung2 = x
y_doi_xung2 = y
z_doi_xung2 = -z
print(f"tọa độ đối xứng qua oxy {x_doi_xung,y_doi_xung,z_doi_xung}")
print(f"tọa độ đối xứng qua oxz {x_doi_xung1,y_doi_xung1,z_doi_xung1}")
print(f"tọa độ đối xứng qua oyz {x_doi_xung2,y_doi_xung2,z_doi_xung2}")
