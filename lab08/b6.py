def BCNN(x,y):
    temp1 = x
    temp2 = y
    while temp1 != temp2:
        if temp1 > temp2:
            temp1 = temp1 - temp2
        elif temp2 > temp1:
            temp2 = temp2 - temp1
    return (x*y)/temp1

x = int(input("nhap x: "))
y = int(input("nhap y: "))
print("boi chung nho nhat cua x va y la",BCNN(x,y))