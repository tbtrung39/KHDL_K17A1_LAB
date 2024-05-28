from packages import is_TamGiac,ChuviTamGiac,S_TamGiac,ChuviHinhVuong,DientichHinhVuong
a = int(input("Nhập vào cạnh a: "))
b = int(input("Nhập vào cạnh b: "))
c = int(input("Nhập vào cạnh c: "))
if is_TamGiac(a,b,c):
    print("Đây là 1 tam giác")
    print(f"Chu vi tam giac là: {ChuviTamGiac(a,b,c)}")
    print(f"diện tích tam giác là: {S_TamGiac(a,b,c)}")
else:
    print("Đây không phải tam giác")

a = int(input("Nhập vào độ dài cạnh a: "))
print(f"Chu vi hình vuông là: {ChuviHinhVuong(a)}")
print(f"Diện tích hình vuông là: {DientichHinhVuong(a)}")