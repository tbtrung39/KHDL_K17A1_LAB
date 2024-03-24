n = int(input("Nhập n:"))
dem =0
for i in range(2,n+1):
    dem=0
    while n%i==0:
        dem+=1
        n//=i
    if dem:
        print(i,end='')
        if dem>1:
            print("^",dem,end='')
        if n>i:
            print("*",end='')
