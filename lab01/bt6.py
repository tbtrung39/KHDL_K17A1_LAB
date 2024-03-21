hieu_dien_the = 220
cuong_do_dong_dien = 2.7
cong_suat = hieu_dien_the * cuong_do_dong_dien
tgian_sd = int(input("Nhập thời gian sử dụng(s): "))
tgian_gio = tgian_sd/ 3600
luong_dien_tieu_thu = cong_suat * tgian_gio / 1000
gia_dien = 7000
tien_dien = luong_dien_tieu_thu * gia_dien
print("Tiền điện phải trả: ",tien_dien)