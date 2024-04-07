s = input("Nhập vào:")
b = 2
t = s[::-1]
kq = 0

for i in range(len(t)):
        kq = kq + int(t[i]) * (b ** i)

print(kq)
