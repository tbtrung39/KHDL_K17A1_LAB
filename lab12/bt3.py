import datetime

def nhapngay():
    try:
        ngay = int(input("nhap ngay: "))
        thang = int(input("nhap thang: "))
        nam = int(input("nhap nam: "))
        ngaynhap = datetime.date(nam, thang, ngay)
        ngaytruoc = ngaynhap - datetime.timedelta(days=1)
        print(f"ngay truoc ngay {ngay}/{thang}/{nam} la: {ngaytruoc.day}/{ngaytruoc.month}/{ngaytruoc.year}")
    except ValueError:
        print("dau vao khong hop le")
    except Exception as e:
        print(f"loi khong xac dinh: {e}")

nhapngay()
