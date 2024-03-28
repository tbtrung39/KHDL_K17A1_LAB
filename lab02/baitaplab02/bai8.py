luong_can_ban = 1350000
he_so1=2.34
he_so2=3.33
he_so3=3.66
he_so4=3.99
tham_nien_cong_tac = float(input("Nhap vao tham nien cong tac: "))
if tham_nien_cong_tac<12:
    luong=he_so1*luong_can_ban
    print("luong nhan vien:", luong)
elif 12<=tham_nien_cong_tac<36:
    luong=he_so2*luong_can_ban
    print("luong nhan vien: ",luong)
elif 36<=tham_nien_cong_tac<60:
    luong=he_so3*luong_can_ban
    print("luong nhan vien:",luong)
elif tham_nien_cong_tac>=60:
    luong=he_so4*luong_can_ban
    print("luong nhan vien:",luong)
else:
    print("error,please try again")