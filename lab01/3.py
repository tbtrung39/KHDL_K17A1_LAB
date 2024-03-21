ban_kinh = int(input("nhập bán kính hình trụ:"))
chieu_cao = int(input("nhập chiểu cao hình trụ"))
pi = 3.14
dien_tich_xung_quanh = 2*pi*ban_kinh*chieu_cao
dien_tich_toan_phan = 2*pi*ban_kinh*chieu_cao + 2*pi*(ban_kinh**2)
the_tich = pi*(ban_kinh**2)*chieu_cao
print("diện tích xung quanh là:",round(dien_tich_xung_quanh,2))
print("diện tích toàn phần là :",round(dien_tich_toan_phan,2))
print("thể tích của hình trụ là:",round(the_tich,2))