a = int(input("Nhập cạnh thứ nhất: "))
b = int(input("Nhập cạnh thứ hai: "))
c = int(input("Nhập cạnh thứ ba: "))
from package import my_Triange
if my_Triange.is_TamGiac(a, b, c):
    print(f"Tam giác có ba cạnh ({a}, {b}, {c})")
    print(f"Chu vi tam giác là: {my_Triange.ChuviTamGiac(a, b, c)}")
    print(f"Diện tích tam giác là: {my_Triange.S_TamGiac(a, b, c)}")
else:
    print("Đây không phải tam giác")


