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

try:
    ngay=int(input('nhap ngay: '))
    thang=int(input('nhap thang: '))
    nam=int(input('nhap nam: '))
    ngay_ke_tiep=ngay_tiep_theo(ngay,thang,nam)
    print(ngay_ke_tiep)
except ValueError:
    print("ngay khong hop le!!!")