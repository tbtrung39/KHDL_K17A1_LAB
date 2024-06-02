import datetime
def tinh_tuan(ngay,thang,nam):
    ngay_trong_nam = datetime.date(nam,thang,ngay).timetuple()
    tuan=(ngay_trong_nam-1)//7 +1
    return tuan
try:
    ngay = int(input("nhap ngay:"))
    thang = int(input("nhap thang:"))
    nam = int(input("nhap nam:"))
    tuan = tinh_tuan(ngay,thang,nam)
    assert ngay >=1 and ngay<=31,"nhap so ngay"
    assert thang >=1 and thang <=12,"nhap thang"
except AssertionError as e:
    print(e)
except ValueError as e:
    print("vui long nhap so nguyen")