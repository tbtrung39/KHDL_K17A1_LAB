import my_Triange

a = float(input("Nhap do dai a: "))
b = float(input("Nhap do dai b: "))
c = float(input("Nhap do dai c: "))

if my_Triange.is_TamGiac(a, b, c):
    print("Day la hinh tam giac")
    chu_vi = my_Triange.Chuvi_TamGiac(a, b, c)
    print("Chu vi tam giac:", chu_vi)
    dien_tich = my_Triange.S_TamGiac(a, b, c)
    print("Dien tich tam giac:", dien_tich)
else:
    print("Day khong phai hinh tam giac")