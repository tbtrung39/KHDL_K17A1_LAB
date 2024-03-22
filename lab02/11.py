ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
    print("Loi!Nhap nam khong nhuan")
else:
    if thang==2:
        so_ngay_trong_thang = 28
    elif thang ==4 or thang ==6 or thang==9 or thang==11:
        so_ngay_trong_thang = 30
    else:
        so_ngay_trong_thang = 31

    if thang < 1 or thang > 12:
        print("Loi.Thang khong hop le")
    elif ngay<1 or ngay> so_ngay_trong_thang:
        print("Loi.Ngay khong hop le")
    else:
        ngay += 1
        if ngay > so_ngay_trong_thang:
            ngay = 1
            thang += 1
            if thang > 12:
                thang = 1
                nam += 1
            print("Ngày tiếp theo là ngày", ngay, "tháng", thang, "năm", nam)