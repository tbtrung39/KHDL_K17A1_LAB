import math
def is_Tamgiac(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True 
    else:
        return False

def Chuvitamgiac(a, b, c):

    if is_Tamgiac(a, b ,c):
        return a + b + c
    else:
        return "Khong phai tam giac"

def S_Tamgiac(a, b, c):
    if is_Tamgiac(a, b, c):
        p = (a + b+ c) / 2
        area =  math.sqrt(p * (p - a) * (p - b) * (p - c))
        return area
    else:
        return "Khong phai tam giac"