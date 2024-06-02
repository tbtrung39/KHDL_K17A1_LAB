from datetime import datetime

while True:
    try:
        day = int(input("Ngày: "))
        month = int(input("Tháng: "))
        year = int(input("Năm: "))
        
        date_input = datetime(year, month, day)
        iso_year, iso_week, iso_weekday = date_input.isocalendar()

        print(f"Ngày {day}/{month}/{year} thuộc tuần thứ {iso_week} trong năm {iso_year}.")
        break
    except ValueError:
        print("Sai, vui lòng nhập lại.")
