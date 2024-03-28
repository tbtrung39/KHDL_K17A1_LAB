n = int(input("Nhập vào n:"))
for i in range(2,n):
    d=0
    for j in range(2,i):
        if i%j==0:
            d=1
    if d==0:
        print(f"{i} là các số nguyên tố bé hơn n")