n = int(input("Nhập số n: "))

if n < 2:
    print("Không phải là số nguyên tố")
else:
    a = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            a = False
            break

    if a:
        print("Là số nguyên tố")
    else:
        b = n
        while True:
            b -= 1
            c = True
            for i in range(2, int(b**0.5) + 1):
                if b % i == 0:
                    c = False
                    break
            if c:
                break
        print(f"Số nguyên tố gần nhất: {b}")