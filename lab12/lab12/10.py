from datetime import datetime

def tinh_khoang_cach(ngay1, thang1, nam1, ngay2, thang2, nam2):
    ngay_bat_dau = datetime(nam1, thang1, ngay1)
    ngay_ket_thuc = datetime(nam2, thang2, ngay2)
    
    # Đổi các ngày về thứ tự để tính khoảng cách
    if ngay_bat_dau > ngay_ket_thuc:
        ngay_bat_dau, ngay_ket_thuc = ngay_ket_thuc, ngay_bat_dau

    # Tính tổng số ngày giữa hai ngày
    tong_so_ngay = (ngay_ket_thuc - ngay_bat_dau).days

    # Tính năm, tháng và ngày
    years = tong_so_ngay // 365
    months = (tong_so_ngay % 365) // 30
    days = (tong_so_ngay % 365) % 30

    return years, months, days

def nhap_ngay():
    try:
        ngay, thang, nam = map(int, input('Nhập ngày (định dạng ngay-thang-nam): ').split('-'))
        return ngay, thang, nam
    except ValueError:
        print('Vui lòng nhập đúng định dạng ngày-thang-nam!')
        return nhap_ngay()

print("Nhập ngày đầu tiên:")
ngay1, thang1, nam1 = nhap_ngay()

print("Nhập ngày thứ hai:")
ngay2, thang2, nam2 = nhap_ngay()

years, months, days = tinh_khoang_cach(ngay1, thang1, nam1, ngay2, thang2, nam2)
print(f'Khoảng cách giữa {ngay1}-{thang1}-{nam1} và {ngay2}-{thang2}-{nam2} là {years} năm, {months} tháng, và {days} ngày.')
