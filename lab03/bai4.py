#câu 4 tìm các số ngto
n = int(input("Nhập một số nguyên dương n: "))
print("Các số nguyên tố nhỏ hơn hoặc bằng", n, "là:")
for i in range(2, n + 1):
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)