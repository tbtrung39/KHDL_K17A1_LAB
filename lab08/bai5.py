def tinh_ucln(a, b):
    """Hàm này sử dụng thuật toán Euclid để tìm UCLN của hai số a và b."""
    while b != 0:
        a, b = b, a % b
    return a

# Nhập số nguyên a và b từ bàn phím
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

# Tính UCLN của a và b
ucln = tinh_ucln(a, b)

# In kết quả
print(f"Ước chung lớn nhất của {a} và {b} là: {ucln}")