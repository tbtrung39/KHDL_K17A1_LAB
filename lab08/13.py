def nam_nhuan(nam):
    if nam% 4 == 0:
        if nam % 100 == 0:
            if nam% 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
nam = int(input("Nhập năm:"))
if nam_nhuan(nam):
    print(f"{nam} là năm nhuận.")
else:
    print(f"{nam} không phải là năm nhuận.")

def xem_thang(thang, nam):
    ngay_31= [1, 3, 5, 7, 8, 10, 12]
    if thang == 2:
        if nam_nhuan(nam):
            return 29
        else:
            return 28
    elif thang in [4, 6, 9, 11]:
        return 30
    elif thang in ngay_31:
        return 31
    else:
        return -1 
thang = int(input("Nhập tháng:"))
ngay_toi_da=xem_thang(thang,nam)
print(f"Tháng {thang} năm {nam} có tối đa {ngay_toi_da} ngày.")
        