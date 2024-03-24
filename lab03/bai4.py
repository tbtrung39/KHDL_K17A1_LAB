n = int(input("Nhập một số nguyên dương n: "))
print(f"Các số nguyên tố bé hơn hoặc bằng {n} là:")
for so in range(2, n + 1):
    is_prime = True
    for i in range(2, int(so**0.5) + 1):
        if so % i == 0:
            flag = False
            break
    if is_prime:       
        print(so, end=" ")