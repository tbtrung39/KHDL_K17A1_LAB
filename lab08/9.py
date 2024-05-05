def math(a,b):
    tong = a + b
    hieu = a - b
    tich = a * b
    if a != 0 and b !=0:
        thuong = a / b
        print(thuong)
    else:
        print(a,b,'>0')
    return print(tong,hieu,tich)
math(0,0)
