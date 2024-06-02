
while True:
    try:
        ngay = int(input("ngay: "))
        thang = int(input("thang: "))
        nam = int(input("nam: "))
        ngay2 = int(input("ngay2: "))
        thang2 = int(input("thang2: "))
        nam2 = int(input("nam2: "))

        # Validate the input dates
        if thang < 1 or thang > 12 or thang2 < 1 or thang2 > 12 or nam < 0 or nam2 < 0:
            raise ValueError

        if thang in (1, 3, 5, 7, 8, 10, 12):
            if ngay < 1 or ngay > 31:
                raise ValueError
        elif thang in (4, 6, 9, 11):
            if ngay < 1 or ngay > 30:
                raise ValueError
        elif thang == 2:
            if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):  # Leap year
                if ngay < 1 or ngay > 29:
                    raise ValueError
            else:
                if ngay < 1 or ngay > 28:
                    raise ValueError

        if thang2 in (1, 3, 5, 7, 8, 10, 12):
            if ngay2 < 1 or ngay2 > 31:
                raise ValueError
        elif thang2 in (4, 6, 9, 11):
            if ngay2 < 1 or ngay2 > 30:
                raise ValueError
        elif thang2 == 2:
            if (nam2 % 4 == 0 and nam2 % 100 != 0) or (nam2 % 400 == 0):  # Leap year
                if ngay2 < 1 or ngay2 > 29:
                    raise ValueError
            else:
                if ngay2 < 1 or ngay2 > 28:
                    raise ValueError

        break

    except ValueError:
        print("Sai. Vui lòng nhập lại.")

# Calculate the difference in days
from datetime import date

date1 = date(nam, thang, ngay)
date2 = date(nam2, thang2, ngay2)

diff = abs((date2 - date1).days)

print(f"Cách nhau: {diff} ngày") 