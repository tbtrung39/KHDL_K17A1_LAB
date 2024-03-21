x = float(input("Nhập tọa độ x của điểm:"))
y = float(input("Nhập toạ độ y của điểm:"))
z = float(input("Nhập tọa độ z của điểm:"))
def diem_doi_xung_oxy(x,y,z):
    return x,y,-z
def diem_doi_xung_oxz(x,y,z):
    return x,-y,z
def diem_doi_xung_oyz(x,y,z):
    return -x,y,z
doi_xung_oxy= diem_doi_xung_oxy(x,y,z)
doi_xung_oxz= diem_doi_xung_oxz(x,y,z)
doi_xung_oyz= diem_doi_xung_oyz(x,y,z)
print("Tọa độ của điểm đối xứng Oxy là:", doi_xung_oxy)
print("Tọa độ của điểm đối xứng Oxz là:", doi_xung_oxz)
print("Tọa độ của điểm đối xứng Oyz là:", doi_xung_oyz)
