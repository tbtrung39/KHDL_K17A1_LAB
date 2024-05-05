def UCLN(x,y):
    temp1 = x
    temp2 = y
    while temp1 != temp2:
        if temp1 > temp2:
            temp1 = temp1 - temp2
        elif temp2 > temp1:
            temp2 = temp2 - temp1
    return temp1

x = int(input("nhap x: "))
y = int(input("nhap y: "))
print("uoc chung lon nhat cua x va y la:",UCLN(x,y))