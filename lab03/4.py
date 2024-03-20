#Viết chương trình in ra tất cả các số nguyên tố bé hơn hoặc bằng n.
n=int(input("moi nhap so n:"))
for i in range(0,n,-1):
    for j in range(0,i):
        if j==0 or j==1:
            continue
        if i%j==0:
            break
    else:
        print("la so nguyen to:")