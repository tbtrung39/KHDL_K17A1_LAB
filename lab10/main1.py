from packages import is_TamGiac,ChuviTamGiac,S_TamGiac
a = int(input("nhập vào cạnh a: "))
b = int(input("nhập vào cạnh b: "))
c = int(input("nhập vào cạnh c: "))
if is_TamGiac(a,b,c):
    print("Là tam giác")
    print(f"Chu vi tam giac là: {ChuviTamGiac(a,b,c)}")
    print(f"diện tích tam giác là: {S_TamGiac(a,b,c)}")
else:
    print("không phải tam giác")