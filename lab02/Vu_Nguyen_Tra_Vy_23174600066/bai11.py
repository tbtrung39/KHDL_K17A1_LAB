
day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))


if month == 12:
    day_trong_month_tiep_theo = 31
else:
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10:
        day_trong_month_tiep_theo = 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        day_trong_month_tiep_theo = 30
    else:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            day_trong_month_tiep_theo = 29
        else:
            day_trong_month_tiep_theo = 28


if day == day_trong_month_tiep_theo:
    day_moi = 1
    if month == 12:
        month_moi = 1
        year_moi = year + 1
    else:
        month_moi = month + 1
        year_moi = year
else:
    day_moi = day + 1
    month_moi = month
    year_moi = year


print('ngày tiếp theo là : ',day_moi,'/',month_moi,'/',year_moi)