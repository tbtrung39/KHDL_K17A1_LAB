#bài a
n = int(input("Nhập n:"))
tong=0
for i in range(1,n+1):
    tong+=(n*(n+1)/2)
print(tong)
#bai b
x=int(input("Nhập n:"))
tong1=0
for i in range(1,n+1,2):
    tong1+=(n+1)*2
print(tong1)
#bài c
y = int(input("Nhập y:"))
tong2=0
for i in range(2,n+1,2):
    tong2+=n*(n+1)
print(tong2)