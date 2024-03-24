import math

a = float(input("Nhập giá trị của a: "))
b = float(input("Nhập giá trị của b: "))
c = float(input("Nhập giá trị của c: "))
d = float(input("Nhập giá trị của d: "))
r = float(input("Nhập giá trị của r: "))

khoang_cach= math.sqrt((c - a)**2 + (d - b)**2)
if khoang_cach > r:
    print("Điểm M nằm ngoài đường tròn.")
elif khoang_cach == r:
    print("Điểm M nằm trên đường tròn.")
else:
    print("Điểm M nằm trong đường tròn.")