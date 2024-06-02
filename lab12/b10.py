from datetime import datetime

while True:
    try:
        ngay = int(input("ngay: "))
        thang = int(input("thang: "))
        nam = int(input("nam: "))
        ngay_2 = int(input("ngay 2: "))
        thang_2 = int(input("thang 2: "))
        nam_2 = int(input("nam 2: "))


        date1 = datetime(nam, thang, ngay)
        date2 = datetime(nam_2, thang_2, ngay_2)

        break
    except ValueError:
        print("sai, vui long nhap lai")


delta = date2 - date1

days = delta.days
years = days // 365
months = (days % 365) // 30
days = (days % 365) % 30

print(f"cach nhau: {days} ngay, {months} thang, {years} nam")
