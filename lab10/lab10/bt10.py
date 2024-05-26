# Import các module từ package hinhhoc
from hinhhoc import is_TamGiac, ChuviTamGiac, S_TamGiac
from hinhhoc import ChuviHinhvuong, DientichHinhvuong

# Nhập ba cạnh của tam giác
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

# Kiểm tra xem ba cạnh có tạo thành tam giác hay không
if is_TamGiac(a, b, c):
    print(f"Chu vi tam giác: {ChuviTamGiac(a, b, c)}")
    print(f"Diện tích tam giác: {S_TamGiac(a, b, c)}")
else:
    print("Ba cạnh a, b, c không tạo thành một tam giác")

# Nhập cạnh của hình vuông
d = float(input("Nhập cạnh hình vuông: "))

# Tính chu vi và diện tích của hình vuông
print(f"Chu vi hình vuông: {ChuviHinhvuong(d)}")
print(f"Diện tích hình vuông: {DientichHinhvuong(d)}")
