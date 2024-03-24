
tong1=0
tong2=0
tong3=0
for n in range(1,999999999999999999999999999):
    if n>0 :      
        n=int(input("nhập số nguyên dương n : "))
        tong1+=n
        tong2+= (2*n+1)
        tong3+=(2*n)
        if n<=0:
            print(f"ta có tổng các biểu thức a) =  {tong1}")
            print(f"ta có tổng các biểu thức b) =  {tong2}")
            print(f"ta có tổng các biểu thức c) =  {tong3}")
            break