n = int(input("Nhập số tháng làm việc: "))
if n < 12:
    luong1 = 2.34 * 1350000
    print("Lương bằng: ", luong1)
if n >= 12 and n < 36:
    luong2 = 3.33 * 1350000
    print("Lương bằng: ", luong2)
if n >= 36 and n < 60:
    luong3 = 3.66 * 1350000
    print("Lương bằng: ", luong3)
if n >= 60:
    luong4 = 3.99 * 1350000
    print("Lương là: ", luong4)