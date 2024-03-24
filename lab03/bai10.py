so = int(input("Nhập vào một số nguyên dương: "))
songuyen = so
print(f"Phân tích thừa số nguyên tố của {so} là: ")
for i in range(2, so + 1):
    tong = 0
    for j in range(2, i+1):
        if i % j == 0:
            co = True
            for k in range(2, int(j/2)+1):
                if j % k == 0:
                    co = False
                    break
            if co:
                while so % j == 0:
                    tong += 1
                    so //= j
    if tong > 0:
        if tong == 1:
            print(f"{i}", end='')
        else:
            print(f"{i}^{tong}", end='')
        if so > 1:
            print(" x ", end='')
        else:
            break