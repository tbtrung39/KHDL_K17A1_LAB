n = int(input("Nhập một số nguyên dương: "))
print("Giá trị tích ")
for i in range(2,n+1):
    dem=0
    if n%i==0:
        dem+=1
        n//=i
    if dem>0:
        if n==1:
            print(f"{i}*{dem}",end="")
        else:
            print(f"{i}*{dem}",end="*")
        if n==1:
            break