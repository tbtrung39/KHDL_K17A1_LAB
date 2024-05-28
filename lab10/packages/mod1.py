import math
def is_TamGiac(a,b,c):
    if a + b > c or b + c > a or a + c > b:
        return True
    else:
        return False

def ChuviTamGiac(a,b,c):
    return a + b + c

def S_TamGiac(a,b,c):
    if not is_TamGiac(a, b, c):
        return None
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
