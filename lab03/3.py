n = int(input("Nhập số n: "))


nt = True
if n <= 1:
    nt = False
else:
    for i in range(2, n):
        if n % i == 0:
            nt = False
            break


if not nt:
    nt_num = n
    while True:
        nt_num -= 1
        if nt_num <= 1:
            break
        nt = True
        for i in range(2, nt_num):
            if nt_num % i == 0:
                nt = False
                break
        if nt:
            break
    print(n, "không phải là số nguyên tố. Số nguyên tố gần nhất là:", nt_num)
else:
    print(n, "là số nguyên tố.")
