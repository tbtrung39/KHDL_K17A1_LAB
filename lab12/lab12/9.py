import datetime

def tinh_tuan_trong_nam(ngay, thang, nam):
    try:
        ngay_nhap = datetime.datetime(nam, thang, ngay)
        tuan_thu = ngay_nhap.isocalendar()[1]
        return tuan_thu
    except ValueError as ve:
        return str(ve)

def nhap_ngay():
    try:
        ngay = int(input('Nhập ngày: '))
        thang = int(input('Nhập tháng: '))
        nam = int(input('Nhập năm: '))
        return ngay, thang, nam
    except ValueError:
        print('Vui lòng nhập đúng định dạng!')
        return nhap_ngay()

ngay, thang, nam = nhap_ngay()
tuan_thu = tinh_tuan_trong_nam(ngay, thang, nam)

if isinstance(tuan_thu, int):
    print(f'Ngày {ngay}/{thang}/{nam} là tuần thứ {tuan_thu} trong năm.')
else:
    print(f'Lỗi: {tuan_thu}')
