from datetime import datetime

while True:
    try:
        day1 = int(input("Ngày 1: "))
        month1 = int(input("Tháng 1: "))
        year1 = int(input("Năm 1: "))
        day2 = int(input("Ngày 2: "))
        month2 = int(input("Tháng 2: "))
        year2 = int(input("Năm 2: "))

        date1 = datetime(year1, month1, day1)
        date2 = datetime(year2, month2, day2)
        break
    except ValueError:
        print("Sai, vui lòng nhập lại.")

delta = date2 - date1

days = delta.days
years = days // 365
months = (days % 365) // 30
days = (days % 365) % 30

print(f"Cách nhau: {days} ngày, {months} tháng, {years} năm")
