def la_nam_nhuan(nam):
    if nam % 4 == 0:
        if nam % 100 == 0:
            if nam % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def ngay_truoc_do(ngay, thang, nam):
    if ngay > 1:
        ngay -= 1
    elif thang in [5, 7, 10, 12]:
        ngay = 30
    elif thang in [2, 4, 6, 8, 9, 11]:
        ngay = 31
    elif thang == 3:
        if la_nam_nhuan(nam):
            ngay = 29
        else:
            ngay = 28
    elif thang == 1:
        ngay = 31
        thang = 12
        nam -= 1
    return ngay, thang, nam

try:
    ngay = int(input("Nhập ngày: "))
    thang = int(input("Nhập tháng: "))
    nam = int(input("Nhập năm: "))

    ngay, thang, nam = ngay_truoc_do(ngay, thang, nam)

    print("Ngày trước đó là:", ngay, "/", thang, "/", nam)

except ValueError:
    print("Lỗi: Bạn cần nhập một số nguyên là ngày, tháng, năm.")
