n = int(input("Nhập vào một số tự nhiên n: "))
print(f"Dãy {n} số nguyên tố đầu tiên là:")
num = 2
so_lg = 0
while so_lg < n:
    is_a = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_a = False
            break
    if is_a:
        print(num, end="\t")
        so_lg += 1
    num += 1
