def is_TamGiac(a, b, c):
    return a + b > c and a + c > b and b + c > a

def ChuviTamGiac(a, b, c):
    if is_TamGiac(a, b, c):
        return a + b + c
    else:
        raise ValueError("Những cạnh này không tạo thành tam giác.")

def S_TamGiac(a, b, c):
    if is_TamGiac(a, b, c):
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return area
    else:
        raise ValueError("Những cạnh này không tạo thành tam giác.")
