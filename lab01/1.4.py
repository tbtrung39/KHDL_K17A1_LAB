U = 220
I = 2.7
thoi_gian = float(input("nhap thoi gian: "))
P = U * I
nang_luong_tieu_thu = P * thoi_gian
tien_dien_phai_tra = (nang_luong_tieu_thu/3600000)*7000
print(f"tien dien phai tra là: {tien_dien_phai_tra:.2f}")