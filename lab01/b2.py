chieu_cao=float(input("nhap chieu cao: "))
ban_kinh=float(input("nhap ban kinh: "))
s_xung_quanh=2*3.14*ban_kinh*chieu_cao
s_day=3.14*(ban_kinh**2)
s_toan_phan=s_xung_quanh+2*s_day
the_tich=3.14*(ban_kinh**2)*chieu_cao
s_xung_quanh=round(s_xung_quanh,2)
s_toan_phan=round(s_toan_phan,2)
the_tich=round(the_tich,2)
print("dien tich xung quanh = ",s_xung_quanh ,"dien tich toan phan = ",s_toan_phan ,"the tich = ",the_tich)