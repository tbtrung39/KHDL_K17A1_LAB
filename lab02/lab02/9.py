gio_bat_dau = int(input("Nhập giờ bắt đầu (từ 5 đến 22): "))
gio_ket_thuc = int(input("Nhập giờ kết thúc (từ 5 đến 22): ")) 
don_gia_3_gio_dau = 100000
so_gio_thue = gio_ket_thuc - gio_bat_dau
if so_gio_thue <= 3:
    tong_tien = so_gio_thue * don_gia_3_gio_dau
else:
    tong_tien = 3 * don_gia_3_gio_dau

        # Đơn giá giảm sau 3 giờ
    don_gia_giam = don_gia_3_gio_dau - (don_gia_3_gio_dau * 0.25)

        # Tính số tiền cho các giờ tiếp theo
    tong_tien += (so_gio_thue - 3) * don_gia_giam

    # Kiểm tra giảm giá nếu thuê từ 11h đến 15h
if 11 <= gio_bat_dau <= 15:
    tong_tien *= 0.9
if 5 <= gio_bat_dau <= gio_ket_thuc <= 22:
    tien_thue_san = tong_tien
    print("Số tiền khách hàng phải trả là:", tien_thue_san, "đ")
else:
    print("Giờ không hợp lệ. Vui lòng nhập lại!")