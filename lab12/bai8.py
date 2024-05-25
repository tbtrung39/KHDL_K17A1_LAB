def kt_nam_nhuan(nam):
    return nam%4==0 and (nam%100!=0 or nam%400 ==0)

def ngay_hom_truoc(ngay,thang,nam):
    cac_ngay_trong_thang=[31,28 if not kt_nam_nhuan(nam) else 29,31,30,31,30,31,31,30,31,30,31]
    if ngay>1:
        return ngay-1, thang, nam
    else: 
        if thang==1:
            return 31,12,nam-1
        else:
            return cac_ngay_trong_thang[thang-2],thang-1,nam

try:
    ngay=int(input('nhap ngay: '))
    thang=int(input('nhap thang: '))
    nam=int(input('nhap nam: '))
    if ngay <1 or thang <1 or thang >12 or nam <1:
        raise ValueError("khong hop le !!!")
    ngay_truoc, thang_truoc, nam_truoc= ngay_hom_truoc(ngay,thang,nam)
    print(f'ngay trc la: {ngay_truoc}/{thang_truoc}/{nam_truoc}')
except ValueError:
    print('loi!!!')
except Exception:
    print('loi!!!')