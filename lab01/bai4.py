hieu_dien_the = 220
cuong_do_dien = 2.7
thoi_gian = int(input("Nhập thời gian sử dụng bóng đèn (giây): "))
gia_dien = 7000

cong_suat = hieu_dien_the * cuong_do_dien

nang_luong_tieu_thu = cong_suat * thoi_gian / 3600

nang_luong_tieu_thu_kwh = nang_luong_tieu_thu / 1000

tien_dien = nang_luong_tieu_thu_kwh * gia_dien

print("Tiền điện phải trả:", tien_dien, "đồng")
