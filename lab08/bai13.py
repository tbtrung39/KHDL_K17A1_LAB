def nam_nhuan(y):
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        return True
    else:
        return False

def so_ngay_toi_da_trong_thang(y, m):
    if m == 2:
        if nam_nhuan(y):
            return 29
        else:
            return 28
    elif m in [4, 6, 9, 11]:
        return 30
    else:
        return 31
y = int(input("nhap nam: "))
m = int(input("Nnhap thang: "))

if nam_nhuan(y):
    print("là năm nhuận.")
else:
    print("không là năm nhuận.")

print(f"Số ngày tối đa trong tháng {m} của năm {y} là: {so_ngay_toi_da_trong_thang(y, m)}")