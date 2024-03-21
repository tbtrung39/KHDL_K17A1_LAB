n = int(input("Nhập số nguyên dương: "))
tong1 = 0
tong2 = 0
tong3 = 0
for i in range(1,n+1):
    tong1 += i**2
    if i % 2 != 0:
        tong2 += i**3
    if i % 2 == 0:
        tong3 += i**4
print("S1 = ", tong1)
print("S2 = ", tong2)
print("S3 = ", tong3)