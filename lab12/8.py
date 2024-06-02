def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

try:
    ngay = int(input("nhap ngay: "))
    thang = int(input("nhap thang:"))
    nam = int(input("nhap nam: "))
except ValueError as e:
    print("Lỗi: Vui lòng nhập một số nguyên hợp lệ.")
else:
    try:
        if thang < 1 or thang > 12 or ngay < 1 or ngay > 31:
            raise ValueError("ngay hoac thang khong hop le")
        if thang in [4, 6, 9, 11] and ngay > 30:
            raise ValueError("Tháng có 30 ngày.")
        if thang == 2:
            if is_leap_year(nam) and ngay > 29:
                raise ValueError("Tháng 2 có 29 ngày.")
            elif not is_leap_year(nam) and ngay > 28:
                raise ValueError("Tháng 2 có 28 ngày.")
        if ngay == 1:
            if thang == 1:
                ngay = 31
                thang = 12
                nam -= 1
            else:
                thang -= 1
                if thang in [1, 3, 5, 7, 8, 10, 12]:
                    ngay = 31
                elif thang in [4, 6, 9, 11]:
                    ngay = 30
                elif thang == 2:
                    if is_leap_year(nam):
                        ngay = 29
                    else:
                        ngay = 28
        else:
            ngay -= 1
        print(f"Ngay truoc do la: {ngay}/{thang}/{nam}")
    except ValueError as e:
        print(e)