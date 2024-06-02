def math(a,b):
    sum = a+b
    hieu = a-b
    tich = a*b
    if a!=0 and b!=0:
        thuong  =a/b
        print(thuong)
    else:
        print(a,b,'lớn hơn 0')
    return print(sum,hieu,tich)
math(0,0)