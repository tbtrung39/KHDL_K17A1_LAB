a = float(input("Nhập vào a: "))
b = float(input("Nhập vào b: "))
c = float(input("Nhập vào c: "))
d = float(input("Nhập vào d: "))
r = float(input("Nhập vào r: "))

binh_phuong_khoang_cach = (c - a) ** 2 + (d - b) ** 2

if binh_phuong_khoang_cach < r ** 2:
    print("M nằm bên trong đường tròn")
elif binh_phuong_khoang_cach == r ** 2:
    print("M nằm trên đường tròn")
else:
    print("M nằm bên ngoài đường tròn")