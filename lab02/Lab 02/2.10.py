a = int(input( " moi ban hap so gio bat dau (tu 5-22):"))
b = int(input( " moi ban hap so gio ket thuc (tu 5-22):"))
if 0<=b-a<=3 :
    don_gia=100000
if b-a>3:
    don_gia= 3*100000 + (b-a-3)*75000
if 11<=a and b<=15:
    don_gia=90000
if  11<=a and b<=15 and b-a>3:
    don_gia = 3*90000+ (b-a-3)*75000
print(" tien san phai tra la :", don_gia)