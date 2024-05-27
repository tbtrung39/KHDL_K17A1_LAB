def is_TamGiac(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

def ChuviTamGiac(a,b,c):
    p = a + b + c
    return p

def S_TamGiac(a,b,c):
    import math
    p2 = (a + b + c)/2
    s = math.sqrt(p2*(p2-a)*(p2-b)*(p2-c))
    return s