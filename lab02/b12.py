import math
a = float(input("Nhập vào giá trị a: "))
b = float(input("Nhập vào giá trị b: "))
c = float(input("Nhập vào giá trị c: "))
d = float(input("Nhập vào giá trị d: "))
r = float(input("Nhập vào giá trị bán kính r: "))

# Tính khoảng cách từ điểm M đến tâm của đường tròn
distance = math.sqrt((c - a)**2 + (d - b)**2)

if distance == r:
    print("Điểm M nằm trên đường tròn")
elif distance > r:
    print("Điểm M nằm ngoài đường tròn")
else:
    print("Điểm M nằm trong đường tròn")