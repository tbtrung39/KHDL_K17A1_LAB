def ucln(a,b):
    temp1 = a
    temp2 = b
    while temp1 != temp2:
        if temp1 > temp2:
            temp1 = temp1 - temp2
        elif temp1 < temp2:
            temp2 = temp2 -temp1
    return temp1
def Bcnn(a,b):
    temp1 = a
    temp2 = b
    while temp1 != temp2:
        if temp1 > temp2:
            temp1 = temp1 - temp2
        elif temp1 < temp2:
            temp2 = temp2 -temp1
    return (a*b)/temp1
def sumdivison(n):
    s=0
    for i in range(1,n):
        if n %i ==0:
            s+=i
    return s
