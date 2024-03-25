#a
n=int(input("Nhập gtri n:"))
tong=0
if n<=0:
    print("Kết thúc!")
for i in range(0,n+1):
    tong+=i
print("S1=",tong)
#b
n=int(input("Nhập gtri n:"))
tong=0
if n<=0:
    print("Kết thúc!")
for i in range(0,n+1):
    if i%2==1:
       tong+=i
print("S2=",tong)
#c
n=int(input("Nhập gtri n:"))
tong=0
if n<=0:
    print("Kết thúc!")
for i in range(0,n+1):
    if i%2==0:
       tong+=i
print("S3=",tong)