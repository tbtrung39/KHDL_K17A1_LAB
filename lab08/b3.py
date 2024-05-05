def so_nguyen_to(x):
    flag =True
    if x ==1 or x <= 0:
        flag = False
        return flag
    for i in range(2,x):
        if x % i ==0:
            flag = False
            return flag
        return flag
    
x = int(input("nhap x: "))
for i in range (x):
    if so_nguyen_to(i):
        print(i,"la so nguyen to")
    
