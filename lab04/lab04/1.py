n=int(input("nhap so nguyen duong n:"))
while n<=0:
    n=int(input("n phai la so nguyen duong. vui long nhap lai:"))

#tinh tong S4
S4=0
i=1
while i<=n:
    S4+=i**2
    i+=1

#tinh tong S5
S5=0
i=1
while i<=n:
    S5+=(2*i+1)**3
    i+=1

#tinh tong S6
S6=0
i=2
while i<=2*n:
    S6 +=i**4
    i+=2

print("tong S4=",S4)
print("tong S5=",S5)
print("tong S6=",S6)