n=int(input("nhap so nguyen duong n= "))
if n<=0:
    print("vui long nhap lai!!!")
else:
    tong=0
    i=1
    while i<=n:
        tong+=i**2
        i+=1
    print("S4 =", tong)
if n<=0:
    print("vui long nhap lai!!!")
else:
    tong=0
    i=1
    while i<=n:
        tong+=i**3
        i+=2
    print("S5 =", tong)
if n<=0:
    print("vui long nhap lai!!!")
else:
    tong=0
    i=1
    while i<=n:
        tong+=i**4
        i*=2
    print("S6 =", tong)