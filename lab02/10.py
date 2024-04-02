gio_bat_dau = int(input("Nhập giờ bắt đầu (từ 5 đến 22): "))
gio_ket_thuc = int(input("Nhập giờ kết thúc (từ 5 đến 22): "))
if 5 <= gio_bat_dau <= 22 and 5 <= gio_ket_thuc <= 22 and gio_bat_dau < gio_ket_thuc:
    don_gia_dau_tien = 100000  
    gio_thue = gio_ket_thuc - gio_bat_dau  
    tong_tien = min(3, gio_thue) * don_gia_dau_tien
    if gio_thue > 3:
        don_gia_giam = don_gia_dau_tien * 0.75  
        gio_con_lai = gio_thue - 3
        tong_tien += gio_con_lai * don_gia_giam
    if 11 <= gio_bat_dau <= 15 and 11 <= gio_ket_thuc <= 15:
        tong_tien *= 0.9
    print("Số tiền phải trả:", tong_tien, "VND")
else:
    print("Giờ không hợp lệ!")