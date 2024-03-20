# kiem tra so hoan hao
n=int(input("moi nhap so nguyen:"))
total=0
for i in range(1,n):
    if n%i==0:
        total+=i
    if n==total:
        print("la so hoan hao")
        break
    else:
        print("khong la so hoan hao")