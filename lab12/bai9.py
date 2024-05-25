def kt_nam_nhuan(nam):
    return nam%4==0 and (nam%100!=0 or nam%400 ==0)

def ngay_trong_nam(ngay,thang,nam):
    cac_ngay_trong_thang=[31,28 if not kt_nam_nhuan(nam) else 29,31,30,31,30,31,31,30,31,30,31]
    dem_ngay=sum(cac_ngay_trong_thang[:thang-1])+ngay
    return dem_ngay

def tuan_trong_nam(ngay,thang,nam):
    dem_ngay=ngay_trong_nam(ngay,thang,nam)
    thu_tu_tuan=dem_ngay//7+1 if dem_ngay%7 !=0 else dem_ngay//7
    return thu_tu_tuan

try:
    ngay=int(input('nhap ngay: '))
    thang=int(input('nhap thang: '))
    nam=int(input('nhap nam: '))
    if ngay<1 or thang<1 or thang>12 or nam<1:
        raise ValueError("khong hop le !!!")
    tuan_thu=tuan_trong_nam(ngay,thang,nam)
    print(f"thuoc tuan thu:{tuan_thu}")
except ValueError:
    print('loi!!!')
except Exception:
    print('loi!!!')