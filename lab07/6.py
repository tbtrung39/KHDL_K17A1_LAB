n=int(input("nhập số tự nhiên : "))
a=0
b=2
while a<n:
    flag=True
    for i in range(2,int(b**0.5)+1):
        if b %i==0:
            flag=False
            break
    if flag:
        print(b)
        a+=1
    b+=1
        