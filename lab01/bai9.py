x = int(input("Giá trị x của tọa độ Oxyz là:"))
y = int(input('Giá trị y của tọa độ Oxyz là:'))
z = int(input("Giá trị z của tọa độ Oxyz là:"))
doi_xung_oxy = x,y,-z
doi_xung_oxz = x,-y,z
doi_xung_oyz = -x,y,z
print("Tọa độ điểm đối xứng qua oxy la:",doi_xung_oxy)
print("Tọa độ điểm đối xứng qua oxz la:",doi_xung_oxz)
print("Tọa độ điểm đối xứng qua oyz la:",doi_xung_oyz)
