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
                if day < 1 or day > 29:
                    raise ValueError
            else:
                if day < 1 or day > 28:
                    raise ValueError
        break
    except ValueError:
        print("Ngày không hợp lệ. Vui lòng nhập lại.")

if day > 1:
    day -= 1
else:
    if month == 1:
        day = 31
        month = 12
        year -= 1
    else:
        month -= 1
        if month in [1, 3, 5, 7, 8, 10, 12]:
            day = 31
        elif month in [4, 6, 9, 11]:
            day = 30
        else:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                day = 29
            else:
                day = 28

print("Ngày trước đó là:", day, month, year)
