thoi_gian = int(input("Nhập thời gian sử dụng bóng đèn (giây): "))
hieu_dien_the = 220 
cuong_do_dien = 2.7  
cong_suat = hieu_dien_the * cuong_do_dien
nang_luong = (cong_suat * thoi_gian) / (3600 * 1000)  
gia_dien = 7000  
tien_dien = nang_luong * gia_dien

# In kết quả
print("Tiền điện phải trả là:", tien_dien, "đồng")