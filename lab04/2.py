import math
n = int(input("Nhập số phần tử n: "))
s1 = 0
for i in range(1, n+1):
    s1 += (-1) ** (i+1) * (1 / i)
print("Tổng s1:", s1)
s2 = 0
for i in range(2, n+2):
    s2 += 1 / ((i-1) * i)
print("Tổng s2:", s2)
s3 = 0
for i in range(2, n+2):
    s3 += 1 / math.sqrt(i)
print("Tổng s3:", s3)