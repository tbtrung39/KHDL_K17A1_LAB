def in_so_nguyen_to(n):
    for i in range(2,n):
        flag=True
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                flag=False
                break
        else:
            flag=True
        if flag:
            print(i)
    
n=int(input("nhap so nguyen duong: "))
in_so_nguyen_to(n)
