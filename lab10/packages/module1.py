import math
def is_TamGiac(a,b,c):
    if a + b > c or a + c > b or b + c > a:
        return True
    else:
        return False
    
def ChuviTamGiac(a,b,c):
    cv = a+b+c
    return cv

def S_TamGiac(a,b,c):
    p = (a + b +c) / 2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return s

def chuviHinhVuong(a):
    p = a * 4
    return p

def Dien_tich_hinh_vuong(a):
    S = a ** 2
    return S
