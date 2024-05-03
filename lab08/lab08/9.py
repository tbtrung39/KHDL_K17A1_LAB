def cong(a, b):
    return a + b
def tru(a, b):
    return a - b
def nhan(a, b):
    return a * b
def chia(a, b):
    if b == 0:
        return "Khong chia duoc cho 0"
    else:
        return a / b
a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
print("Tong:", cong(a, b))
print("Hieu:", tru(a, b))
print("Tich:", nhan(a, b))
print("Thuong:", chia(a, b))
