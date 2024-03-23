kw = float(input("Nhập số KW điện tiêu thụ: "))

if kw <= 100:
    gia = 2000
elif kw <= 200:
    gia = 2500
elif kw <= 300:
    gia = 3000
else:
    gia = 5000

tien_dien = kw * gia
print("Số tiền điện cần thanh toán là: ",tien_dien,"đồng")