n = int(input("Nhập vào một số tự nhiên n: "))

# Tạo tập hợp A (các ước số nguyên tố của n)
A = set()
for i in range(1, n + 1):
    if n % i == 0:
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            A.add(i)
B = set()
for i in range(2, n):
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime and i not in A:
        B.add(i)
print("Tập hợp A:", A)
print("Tập hợp B:", B)
