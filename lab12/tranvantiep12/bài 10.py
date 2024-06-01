from datetime import datetime
from dateutil.relativedelta import relativedelta

def nhap_ngay(ngay_str):
    try:
        ngay = datetime.strptime(ngay_str, "%d-%m-%Y")
        return ngay
    except ValueError:
        print("Định dạng ngày không hợp lệ.")
        return None

def tinh_khoang_cach(ngay1, ngay2):
    if ngay1 > ngay2:
        ngay1, ngay2 = ngay2, ngay1

    khoang_cach = relativedelta(ngay2, ngay1)
    return khoang_cach

def main():
    ngay1_str = "01-01-2020"  # Change to any date in format dd-mm-yyyy
    ngay2_str = "01-06-2023"  # Change to any date in format dd-mm-yyyy
    
    ngay1 = nhap_ngay(ngay1_str)
    ngay2 = nhap_ngay(ngay2_str)
    
    if ngay1 and ngay2:
        khoang_cach = tinh_khoang_cach(ngay1, ngay2)

        print(
            "Khoảng cách giữa hai ngày là: {} năm, {} tháng, {} ngày".format(khoang_cach.years, khoang_cach.months, khoang_cach.days)
        )

main()

