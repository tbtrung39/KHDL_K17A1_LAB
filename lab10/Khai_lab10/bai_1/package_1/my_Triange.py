def Is_TamGiac(a,b,c):
    if a + b > c and a + c > b and b + c > a and a > 0 and b > 0 and c > 0:
        return True
    else: 
        return False

def chuViTamGiac(a,b,c):
    return a + b + c
 
def S_TamGiac(a,b,c):
    import math as m
    q = a + b + c
    return m.sqrt(q * (q - a) * (q - b) * (q - c))
