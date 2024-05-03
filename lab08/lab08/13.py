def nam_nhuan(nam):
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        return True
    else:
        return False
def so_ngay_trong_thang(thang, nam):
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif thang in [4, 6, 9, 11]:
        return 30
    elif thang == 2:
        if nam_nhuan(nam):
            return 29
        else:
            return 28
    else:
        return "Tháng không hợp lệ"
nam = int(input("Nhập năm cần kiểm tra: "))
if nam_nhuan(nam):
    print(nam, "là năm nhuận.")
else:
    print(nam, "không là năm nhuận.")
thang = int(input("Nhập tháng cần kiểm tra: "))
so_ngay = so_ngay_trong_thang(thang, nam)
print(so_ngay)
