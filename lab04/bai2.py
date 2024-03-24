#a
n = int(input("Nhập số phần tử của chuỗi: "))
i = 1
tong = 0
dau = 1
while i <= n:
    if dau == 1:
        tong += 1 / i
    else:
        tong -= 1 / i
    dau *= -1
    i += 1

print("Tổng của chuỗi là:", tong)

#b
n = int(input("Nhập số phần tử của chuỗi: "))
tong = 0
i = 2
while i <= n + 1:
    tong += 1 / ((i-1) * i)
    i += 1

print("Tổng của chuỗi là:", tong)
#c
n = int(input("Nhập số phần tử của chuỗi: "))
tong = 0
i = 2
while i <= n + 1:
    tong += 1 / i ** 0.5
    i += 1

print("Tổng của chuỗi là:", tong)
