n=int(input("Nhập số nguyên N:"))
if n<0:
    print("n phải là số nguyên dương")
else:
    for i in range(2,n+1):
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                break
        else:
            print(i,'',end="")