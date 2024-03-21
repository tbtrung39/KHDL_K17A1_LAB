so_KW = int(input("nhap so kw:"))
if so_KW > 0 and so_KW < 100:
    don_gia = 2000
elif so_KW > 101 and so_KW < 200:
    don_gia = 2500
elif so_KW > 201 and so_KW < 300:
    don_gia = 3000
elif so_KW >300 :
    don_gia = 5000
tien_dien = don_gia * so_KW
print(tien_dien)