import random
n = int(input("nhap so luong phan tu cua tap hop A:"))
A = [random.uniform(-100, 100) for _ in range(n)]
min = 0
max = 0
for x in A:
    if x < min:
        min = x
    if x > max:
        max = x
tong = 0
for x in A:
    tong =+ x
print("tap hop A:", A)
print("phan tu nho nhat:", min)
print("phan tu lon nhat:", max)
print("tong cac phan tu:", tong)