# Nhập số nguyên dương n
n = int(input("Nhập một số nguyên dương n: "))

# Kiểm tra nếu n không là số nguyên dương, dừng chương trình
if n <= 0:
    print("n phải là số nguyên dương. Chương trình đã dừng.")
else:
    # Tính tổng S4 = 1^2 + 2^2 + 3^2 + ... + n^2
    S4 = 0
    for i in range(1, n + 1):
        S4 += i ** 2

    # Tính tổng S5 = 1^3 + 3^3 + 5^3 + ... + (2n+1)^3
    S5 = 0
    for i in range(1, 2 * n + 2, 2):
        S5 += i ** 3

    # Tính tổng S6 = 2^4 + 4^4 + 6^4 + ... + (2n)^4
    S6 = 0
    for i in range(2, 2 * n + 1, 2):
        S6 += i ** 4

    # In kết quả ra màn hình
    print("a) S4 =", S4)
    print("b) S5 =", S5)
    print("c) S6 =", S6)
