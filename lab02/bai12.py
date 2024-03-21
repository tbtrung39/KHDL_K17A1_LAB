import math
a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
c = float(input("Nhập giá trị c: "))
d = float(input("Nhập giá trị d: "))
r = float(input("Nhập giá trị r: "))
khoang_cach = math.sqrt((c - a)**2 + (d - b)**2)
if khoang_cach < r:
    print("Điểm M nằm trong đường tròn.")
elif khoang_cach == r:
    print("Điểm M nằm trên đường tròn.")
else:
    print("Điểm M nằm ngoài đường tròn.")