a = int(input("Nhập 1 số: "))
tong = 0
while a > 0:
    chu_so = a % 10
    tong += chu_so
    a //= 10
print("Tổng các chữ số là ",tong)