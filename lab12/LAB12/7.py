# Bài 1: Tính tổng S1 và S2 sử dụng
def sum_s1(n):
    if n < 1:
        raise ValueError("Giá trị n phải là số nguyên dương.")
    if n == 1:
        return 1
    return n + sum_s1(n - 1)

def sum_s2(n):
    if n < 1:
        raise ValueError("Giá trị n phải là số nguyên dương.")
    if n == 1:
        return 1
    return n ** 2 + sum_s2(n - 1)

try:
    n = int(input("Nhập giá trị n: "))
    if n <= 0:
        raise ValueError("Giá trị n phải là số nguyên dương.")
    s1 = sum_s1(n)
    s2 = sum_s2(n)
    print(f"Tổng S1 = {s1}")
    print(f"Tổng S2 = {s2}")
except ValueError as ve:
    print(f"Lỗi: {ve}")