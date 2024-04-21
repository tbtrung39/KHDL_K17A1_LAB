n = int(input("Nhập số tự nhiên n: "))

A = set()
B = set()
for i in range(1, n + 1):
    if i < 2:
        continue
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime and n % i == 0:
        A.add(i)
for i in range(2, n):
    if i in A:
        continue
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        B.add(i)

print("Tập hợp A:", A)
print("Tập hợp B:", B)