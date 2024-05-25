
def nhap_thong_tin():
    mahang = input("Nhập mã hàng (4 ký tự): ")
    tenhang = input("Nhập tên hàng: ")
    donvitinh = input("Nhập đơn vị tính: ")
    dongia = float(input("Nhập đơn giá: "))
    soluong = int(input("Nhập số lượng: "))
    return {'mahang': mahang, 'tenhang': tenhang, 'donvitinh': donvitinh, 'dongia': dongia, 'soluong': soluong}

def tinh_tien(dongia, soluong):
    return dongia * soluong

def tinh_thue(tien):
    return tien * 0.1

def sap_xep_hang_hoa(hang_hoa_list):
    return sorted(hang_hoa_list, key=lambda x: tinh_thue(tinh_tien(x['dongia'], x['soluong'])), reverse=True)