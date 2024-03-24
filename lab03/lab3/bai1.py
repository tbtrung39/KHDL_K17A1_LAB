# Nhập số phần tử của dãy
n = int(input("Nhập n : "))

sum = 0

for i in range(n + 1):
    gia_tri = 1
    for j in range(i + 1):
        gia_tri = gia_tri * (2 * (j + 1)) / ((2 * j) + 3)
    sum += gia_tri
    print("tong la : ", sum)

kq = sum + 1

# Làm tròn 3 chữ số thập phân
kq = round(kq, 3)

print("Ket qua cua bieu thuc la: ",kq)