s = input("Nhập vào:")
b = 16
t = s[::-1]
kq = 0

for i in range(len(t)):
    if ord(t[i]) < 65:
        kq = kq + int(t[i]) * (b ** i)
    else:
        kq = kq + (ord(t[i]) - 55) * (b ** i)

print(kq)


