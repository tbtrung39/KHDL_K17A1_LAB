n=int(input("nhập số nguyên dương n: "))
if n<=0:
    print("số không hợp lệ!!!")
else:
    S4=0
    for i in range(0,n+1):
        S4+=i**2
    S5=0
    for i in range(0,n+1):
        S5+=(2*i+1)**3
    S6=0
    for i in range(1,n+1):
        S6+=(2*i)**4
    print("S1 =", S4)
    print("S2 =", S5)
    print("S3 =", S6)