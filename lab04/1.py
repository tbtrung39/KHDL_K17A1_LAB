n=int(input("Nhap so nguyen N:"))
s=0
if n<=0:
    print("Vui long nhap lai")
else:
    for i in range (1,n+1):
        s+=i**2
        print("Tong",s)

n=int(input("Nhap so nguyen N:"))
s=0
if n<=0:
    print("Vui long nhap lai")
else:
    for i in range (1,2*n+1,2):
        s+=i**2
        print("Tong",s)

n=int(input("Nhap so nguyen N:"))
s=0
if n<=0:
    print("Vui long nhap lai")
else:
    for i in range (2,2*n,2):
        s+=i**2
        print("Tong",s)
