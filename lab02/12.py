import math
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
d = float(input("Nhập d: "))
r = float(input("Nhập r: "))
khoang_cach_tu_M_den_tam = math.sqrt((c - a)**2 + (d - b)**2)
if khoang_cach_tu_M_den_tam < r:
    print("Điểm M nằm bên trong đường tròn.")
elif khoang_cach_tu_M_den_tam== r:
    print("Điểm M nằm trên đường tròn.")
else:
    print("Điểm M nằm bên ngoài đường tròn.")