def la_nam_nhuan(nam):
    return (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0)
while True:
    try:
        ngay1_str = input("Nhập ngày thứ nhất (định dạng dd-mm-yyyy): ")
        ngay1, thang1, nam1 = map(int, ngay1_str.split('-'))
        if thang1 < 1 or thang1 > 12:
            raise ValueError
        if ngay1 < 1 or ngay1 > 31:
            raise ValueError
        if thang1 in [4, 6, 9, 11] and ngay1 > 30:
            raise ValueError
        if thang1 == 2:
            if la_nam_nhuan(nam1) and ngay1 > 29:
                raise ValueError
            elif not la_nam_nhuan(nam1) and ngay1 > 28:
                raise ValueError
        break
    except ValueError:
        print("ngày không hợp lệ. Vui lòng nhập lại.")

while True:
    try:
        ngay2_str = input("Nhập ngày thứ hai (định dạng dd-mm-yyyy): ")
        ngay2, thang2, nam2 = map(int, ngay2_str.split('-'))
        if thang2 < 1 or thang2 > 12:
            raise ValueError
        if ngay2 < 1 or ngay2 > 31:
            raise ValueError
        if thang2 in [4, 6, 9, 11] and ngay2 > 30:
            raise ValueError
        if thang2 == 2:
            if la_nam_nhuan(nam2) and ngay2 > 29:
                raise ValueError
            elif not la_nam_nhuan(nam2) and ngay2 > 28:
                raise ValueError
        break
    except ValueError:
        print("ngày không hợp lệ. Vui lòng nhập lại.")
def so_ngay_tu_dau_nam(nam, thang, ngay):
    so_ngay = ngay
    for t in range(1, thang):
        if t in [4, 6, 9, 11]:
            so_ngay += 30
        elif t == 2:
            so_ngay += 29 if la_nam_nhuan(nam) else 28
        else:
            so_ngay += 31
    return so_ngay

so_ngay1 = so_ngay_tu_dau_nam(nam1, thang1, ngay1) + nam1 * 365 + nam1 // 4 - nam1 // 100 + nam1 // 400
so_ngay2 = so_ngay_tu_dau_nam(nam2, thang2, ngay2) + nam2 * 365 + nam2 // 4 - nam2 // 100 + nam2 // 400

if so_ngay1 > so_ngay2:
    so_ngay1, so_ngay2 = so_ngay2, so_ngay1

tong_so_ngay = so_ngay2 - so_ngay1

nam = tong_so_ngay // 365
ngay_con_lai = tong_so_ngay % 365

thang = 0
thang_hien_tai = thang1
nam_hien_tai = nam1
while ngay_con_lai > 0:
    so_ngay_trong_thang = 30 if thang_hien_tai in [4, 6, 9, 11] else (29 if thang_hien_tai == 2 and la_nam_nhuan(nam_hien_tai) else 28 if thang_hien_tai == 2 else 31)
    if ngay_con_lai >= so_ngay_trong_thang:
        ngay_con_lai -= so_ngay_trong_thang
        thang_hien_tai += 1
        if thang_hien_tai > 12:
            thang_hien_tai = 1
            nam_hien_tai += 1
        thang += 1
    else:
        break

print(f"Khoảng cách giữa hai ngày là: {nam} năm, {thang} tháng, {ngay_con_lai} ngày")