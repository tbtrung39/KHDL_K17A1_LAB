def ngay_tiep_theo(ngay, thang, nam):
    cac_ngay_trong_thang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if nam % 4 == 0 and (nam % 100 != 0 or nam % 400 == 0):
        cac_ngay_trong_thang[1] = 29  
    if ngay < cac_ngay_trong_thang[thang - 1]:
        return ngay + 1, thang, nam
    elif thang < 12:
        return 1, thang + 1, nam
    else:
        return 1, 1, nam + 1

def tinh_khoang_cach(ngay1, thang1, nam1, ngay2, thang2, nam2):
    ngay1_tong = ngay1 + thang1 * 30 + nam1 * 365
    ngay2_tong = ngay2 + thang2 * 30 + nam2 * 365
    khoang_cach = abs(ngay1_tong - ngay2_tong)

    nam = khoang_cach // 365
    thang = (khoang_cach % 365) // 30
    ngay = (khoang_cach % 365) % 30

    return nam, thang, ngay

try:
    date1 = input('Nhập ngày (ngay-thang-nam): ')
    ngay1, thang1, nam1 = map(int, date1.split('-'))

    date2 = input('Nhập ngày 2 (ngay-thang-nam): ')
    ngay2, thang2, nam2 = map(int, date2.split('-'))

    nam, thang, ngay = tinh_khoang_cach(ngay1, thang1, nam1, ngay2, thang2, nam2)
    print("khoang cach giua 2 ngay la:", nam, "nam,", thang, "thang,", ngay, "ngay")
except ValueError:
    print("khong hop le!!!")
