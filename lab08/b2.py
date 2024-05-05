def UCLN(x,y):
    temp1 = x
    temp2 = y
    while temp1 != temp2:
        if temp1 > temp2:
            temp1 = temp1 - temp2
        elif temp2 > temp1:
            temp2 = temp2 - temp1
    return temp1

x = int(input("nhap vao tu so: "))
y = int(input("nhap vao mau so: "))
print("phan so sau khi rut gon la",int(x/UCLN(x,y)),"/",int(y/UCLN(x,y)))