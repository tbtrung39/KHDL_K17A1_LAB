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

def tinh_ngay_thu_trong_tuan(ngay, thang, nam):
    so_ngay_trong_thang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Nếu là năm nhuận, tháng 2 có 29 ngày
    if la_nam_nhuan(nam):
        so_ngay_trong_thang[1] = 29

    tong_so_ngay = ngay
    for i in range(thang - 1):
        tong_so_ngay += so_ngay_trong_thang[i]

    # Tính ngày thứ trong tuần (tính từ thứ Hai = 1)
    ngay_thu = (tong_so_ngay + nam - 1 + (nam - 1) // 4 - (nam - 1) // 100 + (nam - 1) // 400) % 7

    return ngay_thu

try:
    ngay = int(input("Nhập ngày: "))
    thang = int(input("Nhập tháng: "))
    nam = int(input("Nhập năm: "))

    ngay_thu = tinh_ngay_thu_trong_tuan(ngay, thang, nam)

    if ngay_thu == 0:
        print("Ngày đó là Chủ nhật.")
    else:
        print("Ngày đó là thứ", ngay_thu + 1)

except ValueError:
    print("Lỗi: Bạn cần nhập một số nguyên là ngày, tháng, năm.")
