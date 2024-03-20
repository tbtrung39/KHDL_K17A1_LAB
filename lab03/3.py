n=int(input("moi nhap so nguyen duong:"))
for i in range(0,n,1):
    for j in range(0,i):
        if j==0 or j==1:
            continue
        if i%j==0:
            break
    else:
        print("la so nguyen to:")
        break
