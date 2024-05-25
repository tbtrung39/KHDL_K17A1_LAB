def chuvihinhvuong(a):
    return a*4
def dientichhinhvuong(a):
    return a*a


import math
def Is_TamGiac(a,b,c):
    if a+b>c and a+c>b and c+b>a:
        return True
    return False

def ChuViTamGiac(a,b,c):
    return a+b+c

def dien_tich(a,b,c):
    return math.sqrt(ChuViTamGiac(a,b,c)*(ChuViTamGiac(a,b,c)-a)*(ChuViTamGiac(a,b,c)-c))