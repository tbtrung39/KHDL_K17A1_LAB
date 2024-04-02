n=int(input("nhập so nguyen N:"))
tong=0  
if n<=0:
    print("Nhập lại n")
else:
    for i in range(1,n+1):
        tong+=i**2
        print("S4=1^2+2^2+3^2+.....n^2=",tong)

n=int(input("nhập so nguyen N:"))
tong=0  
if n<=0:
    print("Nhập lại n")
else:
    for i in range(1,n+1,2):
        tong+=i**3
        print("S5=1^3+3^3+5^3+.....n^3=",tong)

n=int(input("nhập so nguyen N:"))
tong=0  
if n<=0:
    print("Nhập lại n")
else:
    for i in range(2,n+1,2):
        tong+=i**4
        print("S6=2^4+4^4+6^4+.....n^=",tong)