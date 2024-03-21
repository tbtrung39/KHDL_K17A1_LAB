ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))
if thang == 2:
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        so_ngay_trong_thang = 29
        if 1 <= ngay < so_ngay_trong_thang:
            ngay += 1
        else:
            ngay = 1
            thang += 1
    else:
        so_ngay_trong_thang = 28
        if 1 <= ngay < so_ngay_trong_thang:
            ngay += 1
        else:
            ngay = 1
            thang += 1
elif thang == 4 or thang == 6 or thang == 9 and thang == 11:
    so_ngay_trong_thang = 30
    if 1 <= ngay < so_ngay_trong_thang:
        ngay += 1
    else:
        ngay = 1
        thang += 1
else:
    so_ngay_trong_thang = 31
    if 1 <= ngay < so_ngay_trong_thang:
        ngay += 1
    else:
        ngay = 1
        thang += 1
if thang == 13:
    thang = 1
    nam += 1
print(f"Ngày tiếp theo là: {ngay}/{thang}/{nam}")
