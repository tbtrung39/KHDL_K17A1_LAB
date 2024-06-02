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

def ngay_ke_tiep(ngay, thang, nam):
    try:
        if thang in [1, 3, 5, 7, 8, 10, 12]:
            if ngay < 31:
                ngay += 1
            elif ngay == 31 and thang < 12:
                ngay = 1
                thang += 1
            elif ngay == 31 and thang == 12:
                ngay = 1
                thang = 1
                nam += 1
        elif thang in [4, 6, 9, 11]:
            if ngay < 30:
                ngay += 1
            elif ngay == 30:
                ngay = 1
                thang += 1
        elif thang == 2:
            if la_nam_nhuan(nam):
                if ngay < 29:
                    ngay += 1
                elif ngay == 29:
                    ngay = 1
                    thang += 1
            else:
                if ngay < 28:
                    ngay += 1
                elif ngay == 28:
                    ngay = 1
                    thang += 1
    except ValueError:
        print("Lỗi: Bạn cần nhập một số nguyên là ngày, tháng, năm.")
    except Exception as e:
        print("Lỗi không xác định:", e)
    return ngay, thang, nam

try:
    ngay = int(input("Nhập ngày: "))
    thang = int(input("Nhập tháng: "))
    nam = int(input("Nhập năm: "))

    ngay, thang, nam = ngay_ke_tiep(ngay, thang, nam)

    print("Ngày kế tiếp là:", ngay, "/", thang, "/", nam)

except ValueError:
    print("Lỗi: Bạn cần nhập một số nguyên là ngày, tháng, năm.")
