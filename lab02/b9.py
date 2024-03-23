kw = int(input("Nhập số KW điện tiêu thụ là:"))
if kw > 300:
    don_gia1 = 5000
    tien_dien1 = kw * don_gia1
    print("Số tiền điện phải trả là:",tien_dien1)
if kw >= 201 and kw <= 300:
    don_gia2 = 3000
    tien_dien2 = kw * don_gia2
    print("Số tiền điện phải trả là:",tien_dien2)
if kw >= 101 and kw <= 200:
    don_gia3 = 2500
    tien_dien3 = kw * don_gia3
    print("Số tiền điện phải trả là:",tien_dien3)
if kw >= 0 and kw <= 100:
    don_gia4 = 2000
    tien_dien4 = kw * don_gia4
    print("Số tiền điện phải trả là:",tien_dien4)