def doc_va_tinh_tong_so_le(ten_tap_tin):
    tong = 0
    try:
        file = open(ten_tap_tin, 'r')  # Mở tệp tin ở chế độ đọc
    except FileNotFoundError:
        print(f"Tệp tin '{ten_tap_tin}' không tồn tại. Vui lòng kiểm tra lại tên tệp tin và đường dẫn.")
        return tong

    for dong in file:
        cac_so = dong.split()  # Tách các số trong dòng dựa trên khoảng trắng
        for so in cac_so:
            so_nguyen = int(so)  # Chuyển đổi chuỗi sang số nguyên
            if so_nguyen % 2 != 0:  # Kiểm tra xem số đó có phải số lẻ không
                tong += so_nguyen  # Nếu lẻ, thêm vào tổng
    file.close()  # Đóng tệp tin
    return tong

# Sử dụng hàm
ten_tap_tin = 'dayso.dat'
tong_cac_so_le = doc_va_tinh_tong_so_le(ten_tap_tin)
print(f"Tổng các số lẻ trong tệp tin là: {tong_cac_so_le}")
