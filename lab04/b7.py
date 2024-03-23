m=int(input("nhap m: "))
n=int(input("nhap n: "))
temp1 =m
temp2 =n
while temp1 != temp2:
    if temp1 > temp2:
        temp1 = temp1 - temp2
    else:
        temp2= temp2 - temp1
BCNN=(m*n)/temp1
print("boi chung nho nhat la",BCNN)