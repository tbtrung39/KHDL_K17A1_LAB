so_nguyen = int(input("Nhập số nguyên n: "))
tap_so_nguyen_to = set()
for i in range(2, so_nguyen + 1):
    if so_nguyen % i == 0:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            tap_so_nguyen_to.add(i)

tap_so_nguyen_toi_thieu = set()
for i in range(2, so_nguyen):
    if so_nguyen % i != 0:
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            tap_so_nguyen_toi_thieu.add(i)

print("Tập số nguyên tố là:", tap_so_nguyen_to)
print("Tập số nguyên tố nhỏ nhất là:", tap_so_nguyen_toi_thieu)