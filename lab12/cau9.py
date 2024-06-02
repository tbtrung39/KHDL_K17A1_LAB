import datetime

def tinh_tuan_trong_nam(ngay, thang, nam):
    ngay_trong_nam = datetime.date(nam, thang, ngay).timetuple().tm_yday
    so_tuan = (ngay_trong_nam - 1) // 7 + 1
    return so_tuan

try:
    ngay = int(input("Nhap ngay: "))
    thang = int(input("Nhap thang: "))
    nam = int(input("Nhap nam: "))

    tuan = tinh_tuan_trong_nam(ngay, thang, nam)
    print("Ngay do thuoc tuan thu:", tuan)

except ValueError:
    print("Loi: Hay nhap so nguyen cho ngay, thang va nam.")
except Exception as e:
    print('Loi khong xac dinh:', e)