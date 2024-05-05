def so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Nhập một số nguyên dương n: "))
print("Các số nguyên tố nhỏ hơn", n, "là:")
for i in range(2, n):
    if so_nguyen_to(i):
        print(i, end=" ")