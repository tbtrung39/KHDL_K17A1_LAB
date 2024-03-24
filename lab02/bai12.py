a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
c = float(input("Nhập giá trị c: "))
d = float(input("Nhập giá trị d: "))
r = float(input("Nhập giá trị r: "))

s1 = (c - a)**2 + (d - b)**2

if s1 < r**2:
    print(f"Điểm M({c},{d}) nằm bên trong đường tròn.")
elif s1 == r**2:
    print(f"Điểm M({c},{d}) nằm trên đường tròn.")
else:
    print(f"Điểm M({c},{d}) nằm ngoài đường tròn.")