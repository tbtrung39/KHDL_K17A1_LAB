import math
a = float(input("Nhập a (hoành độ tâm của đường tròn): "))
b = float(input("Nhập b (tung độ tâm của đường tròn): "))
r = float(input("Nhập r (bán kính của đường tròn): "))
c = float(input("Nhập c (hoành độ điểm M): "))
d = float(input("Nhập d (tung độ điểm M): "))
khoang_cach = math.sqrt((c - a)**2 + (d - b)**2)
if khoang_cach < r:
    print("Điểm M nằm bên trong đường tròn.")
elif khoang_cach == r:
    print("Điểm M nằm trên đường tròn.")
else:
    print("Điểm M nằm ngoài đường tròn.")