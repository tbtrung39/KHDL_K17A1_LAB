import math
thoi_gian_su_dung = float(input("Nhập thời gian sử dụng bóng đèn (giây): "))
hieu_dien_the = float(input("Nhập hiệu điện thế (V): "))
cuong_do_dien = float(input("Nhập cường độ dòng điện (A): "))

thoi_gian_su_dung_gio = thoi_gian_su_dung / 3600  

cong_suat = hieu_dien_the * cuong_do_dien / 1000

luong_dien_tieu_thu = cong_suat * thoi_gian_su_dung_gio

gia_tien_dien = luong_dien_tieu_thu * 7000

print("Tiền điện phải trả là:", gia_tien_dien, "VNĐ")
