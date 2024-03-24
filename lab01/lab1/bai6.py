t = int(input("Nhập thời gian sử dụng bóng đèn (giây): "))
#Tính công suất điện P=U.I
#công suất tiêu thụ điện A=P.t(h)
#Kết hợp A=U.I.t(h)
cong_suat_tieu_thu = 220 * 2.7 * (t/3600)
tien_dien = cong_suat_tieu_thu * 7000
print(f"Tiền điện phải trả: {round(tien_dien,2)} VNĐ")

