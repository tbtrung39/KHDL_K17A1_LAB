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

def tinh_so_ngay_trong_thang(thang, nam):
    so_ngay_trong_thang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if la_nam_nhuan(nam) and thang == 2:
        return 29
    else:
        return so_ngay_trong_thang[thang - 1]

def tinh_khoang_cach_ngay(ngay1, thang1, nam1, ngay2, thang2, nam2):
    # Tính tổng số ngày từ ngày 1/1/1 đến ngày đầu tiên
    tong_so_ngay_1 = ngay1
    for i in range(thang1 - 1):
        tong_so_ngay_1 += tinh_so_ngay_trong_thang(i + 1, nam1)
    for i in range(1, nam1):
        if la_nam_nhuan(i):
            tong_so_ngay_1 += 366
        else:
            tong_so_ngay_1 += 365

    # Tính tổng số ngày từ ngày 1/1/1 đến ngày thứ hai
    tong_so_ngay_2 = ngay2
    for i in range(thang2 - 1):
        tong_so_ngay_2 += tinh_so_ngay_trong_thang(i + 1, nam2)
    for i in range(1, nam2):
        if la_nam_nhuan(i):
            tong_so_ngay_2 += 366
        else:
            tong_so_ngay_2 += 365

    # Tính số ngày chênh lệch giữa hai ngày
    so_ngay_chenh_lech = abs(tong_so_ngay_2 - tong_so_ngay_1)

    # Tính số năm, tháng, ngày chênh lệch
    so_nam = so_ngay_chenh_lech // 365
    so_ngay_chenh_lech %= 365
    so_thang = 0
    for i in range(1, 13):
        so_ngay_trong_thang_i = tinh_so_ngay_trong_thang(i, nam1)
        if so_ngay_chenh_lech - so_ngay_trong_thang_i >= 0:
            so_thang += 1
            so_ngay_chenh_lech -= so_ngay_trong_thang_i
        else:
            break

    return so_nam, so_thang, so_ngay_chenh_lech

def kiem_tra_dinh_dang_ngay(ngay):
    try:
        ngay, thang, nam = map(int, ngay.split('-'))
        if thang < 1 or thang > 12 or ngay < 1 or ngay > tinh_so_ngay_trong_thang(thang, nam) or nam < 1:
            return False
        else:
            return True
    except ValueError:
        return False

try:
    ngay1 = input("Nhập ngày thứ nhất (dd-mm-yyyy): ")
    ngay2 = input("Nhập ngày thứ hai (dd-mm-yyyy): ")

    if not (kiem_tra_dinh_dang_ngay(ngay1) and kiem_tra_dinh_dang_ngay(ngay2)):
        raise ValueError("Định dạng ngày không hợp lệ.")

    ngay1, thang1, nam1 = map(int, ngay1.split('-'))
    ngay2, thang2, nam2 = map(int, ngay2.split('-'))

    so_nam, so_thang, so_ngay = tinh_khoang_cach_ngay(ngay1, thang1, nam1, ngay2, thang2, nam2)

    print("Hai ngày đó cách nhau:", so_nam, "năm,", so_thang, "tháng và", so_ngay, "ngày.")

except ValueError as e:
    print("Lỗi:", e)
