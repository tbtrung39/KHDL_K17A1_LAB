from pk10 import modul10
a = float(input("Nhập cạnh a của hình vuông: "))
print("Chu vi hình vuông là:", modul10.chuvihinhvuong(a))
print("Diện tích hình vuông là:", modul10.dientichhinhvuong(a))

a = float(input("Nhập cạnh a của tam giác: "))
b = float(input("Nhập cạnh b của tam giác: "))
c = float(input("Nhập cạnh c của tam giác: "))
print("Chu vi tam giác là:", modul10.ChuViTamGiac(a, b, c))
print("Diện tích tam giác là:", modul10.dien_tich(a, b, c))
print("Là tam giác không:", modul10.Is_TamGiac(a, b, c))