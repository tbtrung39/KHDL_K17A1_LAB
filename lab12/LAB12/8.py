import datetime
def nhapngay():
    try:
        ngay = int(input("Nhập ngày: "))
        thang = int(input("Nhập tháng: "))
        nam = int(input("Nhập năm: "))
        ngaynhap = datetime(nam, thang, ngay)
        ngaytruoc = ngaynhap - datetime(days=1)
        print(f"Ngày trước ngày {ngay}/{thang}/{nam} là: {ngaytruoc.day}/{ngaytruoc.month}/{ngaytruoc.year}")
    except ValueError:
        print("Đầu vào không hợp lệ")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")

nhapngay()