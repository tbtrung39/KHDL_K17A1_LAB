import math
def  la_tram_giac(a,b,c):
    if a + b > c or a + c > b or b + c > a:
        return True
    else:
        return False
    
def chu_vi(a, b, c):
    p = a + b + c
    return p

def dien_tich(a , b, c):
    p = ( a + b + c) / 2
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return S
