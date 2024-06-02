from datetime import datetime
while True:
    try:
        ngay = int(input("Ngày: "))
        thang = int(input("Tháng: "))
        nam = int(input("Năm: "))

        date = datetime(nam, thang, ngay)

        iso_year, iso_week, iso_weekday = date.isocalendar()

        print(f"Ngày {ngay}/{thang}/{nam} thuộc tuần thứ {iso_week} trong năm {iso_year}.")
        break
    except ValueError:
        print("Sai")