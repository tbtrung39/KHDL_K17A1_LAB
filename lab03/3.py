n=int(input("nhập số nguyên dương n: "))
for i in range(n,1,-1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print("số nguyên tố là: ",i )
        break