TNCT= int(input("nhap tham nien cong tac cua nhan vien:  "))
luong_can_ban= 1350000
if TNCT <0:
    print("vui long nhap lai")
else:
    if TNCT <12:
        he_so=2.34
    elif TNCT >=12 and TNCT < 36:
        he_so= 3.33
    elif TNCT>=36 and TNCT <60:
        he_so=3.66
    else:
        he_so=3.99
    luong= he_so*luong_can_ban
    print("luong cua nhan vien do la: ",luong,"dong")