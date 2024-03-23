n = int(input("Nhập n:"))
tong =0
for i in range(1,n+1):
    tong+=i**2
print(tong)
#bai 2
y = int(input("Nhập y:"))
tong1=0
for i in range(1,n+1,2):
    tong1+=i**3
print(tong1)
#bai 3
x = int(input("Nhập x:"))
tong2=0
for i in range(2,n+1,2):
    tong2+=i**4
print(tong2)