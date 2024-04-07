S=input("nhap chuoi ki tu:")
ktra=""
for i in S:
    if i.isdigit():
        ktra+=i
        print(i)
    continue
n=int(ktra)
tong=0
for i in range(1 , int(n/2) + 1):
    if n%i==0:
        tong+=i
if tong==n:
    print("la so hoan hao",n)
else:
    print("không la so hoan hao",n)