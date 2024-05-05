def cong(a, b):
    return a + b

def tru(a, b):
    return a - b

def nhan(a, b):
    return a * b

def chia(a, b):
    if b != 0:
        return a / b
    else:
        return "Không thể chia cho 0"

a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))

print("Kết quả cộng:", cong(a, b))
print("Kết quả trừ:", tru(a, b))
print("Kết quả nhân:", nhan(a, b))
print("Kết quả chia:", chia(a, b))