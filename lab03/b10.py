so_nguyen = int(input("Nhập một số nguyên dương: "))
if so_nguyen > 0:
    print(f"Phân tích thừa số nguyên tố của {so_nguyen} là: ", end='')
    i = 2
    while i <= so_nguyen:
        if so_nguyen % i == 0:
            print(i, end='')
            so_nguyen //= i
            if so_nguyen > 1:
                print(' * ', end='')
            i = 1
        i += 1
else:
    print("Vui lòng nhập số nguyên dương.")