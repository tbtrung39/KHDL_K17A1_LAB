def tinh_tien_dien(cong_suat, thoi_gian, gia_dien):
    # Tính tiền điện
    tien_dien = (cong_suat * thoi_gian / 1000) * gia_dien
    return tien_dien

def main():
    # Hiệu điện thế (V)
    hieu_dien_the = 220
    # Cường độ dòng điện (A)
    cuong_do_dong_dien = 2.7
    # Thời gian sử dụng (giây)
    thoi_gian = float(input("Nhập thời gian sử dụng bóng đèn (giây): "))
    # Giá tiền điện (đồng/kWh)
    gia_dien = 7000

    # Tính công suất của bóng đèn (W)
    cong_suat = hieu_dien_the * cuong_do_dong_dien

    # Tính tiền điện
    tien_dien = tinh_tien_dien(cong_suat, thoi_gian, gia_dien)

    # In kết quả
    print("Tiền điện phải trả là:", tien_dien, "đồng")

if __name__ == "__main__":
    main()