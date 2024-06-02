while True:
    try:
        day = int(input("Ngày:"))
        month = int(input("Tháng:"))
        year = int(input("Năm:"))
        if day < 0 or month < 0 or month > 12 or year < 0:
            raise ValueError
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if day > 31 or day < 0:
                raise ValueError
        elif month in [4, 6, 9, 11]:
            if day > 30:
                raise ValueError
        elif month == 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                if day < 29:
                    raise ValueError
            else:
                if day > 28:
                    raise ValueError
        break
    except ValueError:
        print("Ngày không hợp lệ. Vui lòng nhập lại.")

days_in_month = 31 if month in [1, 3, 5, 7, 8, 10, 12] else 30 if month in [4, 6, 9, 11] else 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28

if day < days_in_month:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1

print("Ngày tiếp theo là:", day, month, year)
