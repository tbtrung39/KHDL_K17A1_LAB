#câu 6 tổng bậc 3
so_luong = int(input("Nhập số nguyên dương n: "))
tong_bac_ba = 0

for i in range(1, so_luong + 1):
    tong_bac_ba += i ** 3
print("Tổng bậc ba của", so_luong, "số nguyên đầu tiên là:", tong_bac_ba)
