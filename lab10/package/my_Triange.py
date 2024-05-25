import math

def is_TamGiac(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        return True
    else:
        return False

def ChuviTamGiac(a, b, c):
    return a + b + c

def S_TamGiac(a, b, c):
    if is_TamGiac(a, b, c):
        p = ChuviTamGiac(a, b, c) / 2
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return area
    else:
        return "Không phải là tam giác"

# Example usage
a = float(input("Nhập độ dài cạnh a: "))
b = float(input("Nhập độ dài cạnh b: "))
c = float(input("Nhập độ dài cạnh c: "))

if is_TamGiac(a, b, c):
    print(f"Chu vi tam giác là: {ChuviTamGiac(a, b, c)}")
    print(f"Diện tích tam giác là: {S_TamGiac(a, b, c)}")
else:
    print("Ba cạnh đã nhập không tạo thành một tam giác.")


