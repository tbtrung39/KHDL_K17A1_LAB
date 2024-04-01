ban_kinh = float(input("nhap ban kinh"))
chieu_cao = float(input("nhap chieu cao"))
dien_tich_xung_quanh = 2*3.14*ban_kinh*chieu_cao
print(f"dien tich xung quanh la: {dien_tich_xung_quanh:.2f}")
dien_tich_toan_phan = dien_tich_xung_quanh*2*3.14*(ban_kinh**2)
print(f"dien toan phan la: {dien_tich_toan_phan:.2f}")
the_tich = 3.14*(ban_kinh**2)*chieu_cao
print(f"the tich la: {the_tich:.2f}")