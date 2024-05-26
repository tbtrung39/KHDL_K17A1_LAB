import doicoso1, dolcoso2

# Sử dụng các hàm từ module doicoso1
so_nguyen = doicoso1.nhap_va_in_so_nguyen()
doicoso1.chuyen_sang_nhi_phan(so_nguyen)
doicoso1.chuyen_sang_bat_phan(so_nguyen)
doicoso1.chuyen_sang_thap_luc_phan(so_nguyen)

# Sử dụng các hàm từ module dolcoso2
chuoi = input("Nhập một chuỗi ký tự: ")
chuoi_hop_le = dolcoso2.loai_bo_ky_tu_khong_hop_le(chuoi)
co_so = dolcoso2.xac_dinh_co_so(chuoi_hop_le)

if co_so == 2:
    dolcoso2.chuyen_co_so2_sang_co_so10(chuoi_hop_le)
elif co_so == 8:
    dolcoso2.chuyen_co_so8_sang_co_so10(chuoi_hop_le)
elif co_so == 16:
    dolcoso2.chuyen_co_so16_sang_co_so10(chuoi_hop_le)
else:
    print(f"Chuỗi '{chuoi_hop_le}' không thuộc cơ số 2, 8 hoặc 16 hợp lệ.")
