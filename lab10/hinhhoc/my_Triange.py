import math

def is_TamGiac(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


def ChuviTamGiac(a, b, c):
    if is_TamGiac(a, b, c):
        return a + b + c
    else:
        print("Ba cạnh a, b, c không tạo thành một tam giác")

def S_TamGiac(a, b, c):
    if is_TamGiac(a, b, c):
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))
    else:
        print("Ba cạnh a, b, c không tạo thành một tam giác")