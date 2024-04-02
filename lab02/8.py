tnct = float(input("Nhap tham nien cong tac: "))
if tnct < 12:
    he_so = 2.34
    luong = he_so * 1350000
elif tnct >=12 and tnct < 36:
    he_so = 3.33
    luong = he_so * 1350000
elif tnct >= 36 and tnct < 60:
    he_so = 3.66
    luong = he_so * 1350000
else:
    he_so = 3.99
    luong = he_so * 1350000
print("luong cua nhan vien dua theo tham nien cong tac: ", luong)