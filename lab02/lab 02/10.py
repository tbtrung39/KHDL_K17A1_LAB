bat_dau = int(input("nhập giờ vào thuê với giờ 24:"))
ket_thuc = int(input("nhập giờ kết thúc với giờ 24:"))
thoi_gian_thue = ket_thuc - bat_dau
if thoi_gian_thue <= 3:
    gia_phai_tra = thoi_gian_thue *100000
    print("phải trả: ", gia_phai_tra)

gia = 3 * 100000 + (thoi_gian_thue - 3) * 75000
print("giá phải trả: ", gia )

if thoi_gian_thue >= 11 and thoi_gian_thue <= 15:
    gia_moi = (3 * 100000 + (thoi_gian_thue - 3) * 75000) * 0.9
    print("giá phải tả", gia_moi)
if bat_dau < 5:
    print("Sân chưa mở cửa")
if ket_thuc > 22:
    print("Snaa đã đóng cửa")