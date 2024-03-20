# tim cac so hoan hao
n=int(input("moi nhap so nguyen n:"))
total=0
for i in range(1,n):
    if n%i==0:
        sum+=i
    if n==sum:
        print("la so hoan hao")
        break
    else:
        print("khong la so hoan hao")