ki_tu = input("nhap chuoi ki tu: ")
s=""
for i in ki_tu:
    if i.isdigit():
        s+=i
x=int(s)
sum=0
for i in range(1,x):
    if x % i ==0:
        sum+=i
if sum==x:
    print(x,"la so hoan hao")
else:
    print(x,"khong la so hoan hao")