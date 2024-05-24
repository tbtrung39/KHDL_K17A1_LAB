from __pycache__ import my_square,my_triange
a = float(input("Nhập cạnh a của hình vuông: "))
print("Chu vi hình vuông là:", my_triange.chuvihinhvuong(a))
print("Diện tích hình vuông là:", my_triange.dientichhinhvuong(a))

a = float(input("Nhập cạnh a của tam giác: "))
b = float(input("Nhập cạnh b của tam giác: "))
c = float(input("Nhập cạnh c của tam giác: "))
print("Chu vi tam giác là:", my_square.ChuViTamGiac(a, b, c))
print("Diện tích tam giác là:", my_square.dien_tich(a, b, c))
print("Là tam giác không:", my_square.Is_TamGiac(a, b, c))