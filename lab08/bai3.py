def la_so_nguyen_to(x):
    """Hàm kiểm tra x có phải là số nguyên tố không.
    Một số nguyên tố là số lớn hơn 1 và chỉ chia hết cho 1 và chính nó."""
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def in_so_nguyen_to(n):
    """Hàm in ra các số nguyên tố nhỏ hơn n."""
    for i in range(2, n):
        if la_so_nguyen_to(i):
            print(i, end=' ')

# Nhập giá trị n từ người dùng
n = int(input("Nhập n: "))

# In ra các số nguyên tố nhỏ hơn n
print(f"Các số nguyên tố nhỏ hơn {n} là:")
in_so_nguyen_to(n)