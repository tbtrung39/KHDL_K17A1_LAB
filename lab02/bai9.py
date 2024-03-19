so_kw=int(input("nhập số KW diện tiêu thụ: "))
if so_kw >0 and so_kw <=100:
    don_gia1=2000
    tien_dien=so_kw*don_gia1
    print("số tiền điện là:", tien_dien)
if so_kw >100 and so_kw <=200:
    don_gia2=2500
    tien_dien=so_kw*don_gia2
    print("số tiền điện là:", tien_dien)
if so_kw >200 and so_kw <=300:
    don_gia3=3000
    tien_dien=so_kw*don_gia3
    print("số tiền điện là:", tien_dien)
if so_kw >300:
    don_gia4=2000
    tien_dien=so_kw*don_gia4
    print("số tiền điện là:", tien_dien)
else:
    print("giá trị KW không hợp lệ")