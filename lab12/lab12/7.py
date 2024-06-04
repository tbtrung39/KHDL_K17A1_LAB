from datetime import datetime, timedelta

def nhap_ngay():
    try:
        ngay, thang, nam = map(int, input('Nhập ngày (định dạng ngay-thang-nam): ').split('-'))
        return datetime(nam, thang, ngay)
    except ValueError:
        print('Vui lòng nhập đúng định dạng ngày-thang-nam!')
        return nhap_ngay()

def ngay_ke_tiep(ngay_hien_tai):
    ngay_ke_tiep = ngay_hien_tai + timedelta(days=1)
    return ngay_ke_tiep

def main():
    ngay_hien_tai = nhap_ngay()
    ngay_ket_qua = ngay_ke_tiep(ngay_hien_tai)
    print(f'Ngày kế tiếp của {ngay_hien_tai.strftime("%d-%m-%Y")} là {ngay_ket_qua.strftime("%d-%m-%Y")}')
main()
