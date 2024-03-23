#cau a
x = int(input("Nhập x:"))
tong=0
i=1
dau=1
while i<=x:
    tong+=dau*1/i
    i+=1
    dau*=-1
print(tong)
#cau b
n = int(input("Nhập n:"))
tong=0
i=2
while i<=n+1:
    tong+=1/(i*(i-1))
    i+=1
print(tong)
#cau c
import math
n = int(input("Nhập n:"))
tong=0
i=2
while i<=n+1:
    tong+=1/(math.sqrt(i))
    i+=1
print(tong)
