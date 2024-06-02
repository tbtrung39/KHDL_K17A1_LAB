from datetime import datetime

while True:
    try:
        ngay = int(input("Ngay: "))
        thang = int(input("Thang: "))
        nam = int(input("Nam: "))

        date = datetime(nam, thang, ngay)

        iso_year, iso_week, iso_weekday = date.isocalendar()
        
        print(f"Ngay {ngay}/{thang}/{nam} thuoc tuan thu {iso_week} trong nam {iso_year}.")
        break
    except ValueError:
        print("Sai, vui long nhap lai.")