he_so=float(input("Nhap so thang TNCT cua nhan vien:"))
luong_can_ban=1350000
luong=he_so*luong_can_ban
if he_so<12:
    he_so=2.34
    print('Luong cua nhan vien do la :',luong)
elif he_so>=12 and he_so<36:
    he_so=3.33
    print('Luong cua nhan vien do la :',luong)
elif he_so>=36 and he_so<60:
    he_so=3.66
    print('Luong cua nhan vien do la :',luong)
elif he_so>=60:
    he_so=3.99
    print('Luong cua nhan vien do la :',luong)
else:
    print("Loi")