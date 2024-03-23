day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10:
    if day < 31:
        next_day = day + 1
    else:
        next_day = 1
elif month == 4 or month == 6 or month == 9 or month == 11:
    if day < 30:
        next_day = day + 1
    else:
        next_day = 1
elif month == 2:
    if day < 28:
        next_day = day + 1
    else:
        next_day = 1
else:  # Tháng 12
    if day < 31:
        next_day = day + 1
    else:
        next_day = 1

print("Ngày tiếp theo là ngày", next_day, "tháng", month)