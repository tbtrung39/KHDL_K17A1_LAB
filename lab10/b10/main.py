from pk10 import chuvi_hinh_vuong,chuvi_tam_giac,dien_tich_hinh_vuong,dien_tich_tam_giac,la_tam_giac
a = float(input("Nhập cạnh a của hình vuông: "))
print("Chu vi hình vuông là:", chuvi_hinh_vuong(a))
print("Diện tích hình vuông là:", dien_tich_hinh_vuong(a))

a = float(input("Nhập cạnh a của tam giác: "))
b = float(input("Nhập cạnh b của tam giác: "))
c = float(input("Nhập cạnh c của tam giác: "))
print("Chu vi tam giác là:", chuvi_tam_giac(a, b, c))
print("Diện tích tam giác là:", dien_tich_tam_giac(a, b, c))
print("Là tam giác không:", la_tam_giac(a, b, c))
