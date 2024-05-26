def nhap_hang_hoa():
    ma_hang = input("Nhập mã hàng: ")
    ten_hang = input("Nhập tên hàng: ")
    don_vi_tinh = input("Nhập đơn vị tính: ")
    don_gia = float(input("Nhập đơn giá: "))
    so_luong = int(input("Nhập số lượng: "))
    thanh_tien = don_gia * so_luong
    thue = int(thanh_tien * 0.1)
    return {'ma_hang': ma_hang, 'ten_hang': ten_hang, 'don_vi_tinh': don_vi_tinh, 'don_gia': don_gia, 'so_luong': so_luong, 'thanh_tien': thanh_tien, 'thue': thue}

def sap_xep_theo_thue(danh_sach_hang_hoa):
    return sorted(danh_sach_hang_hoa, key=lambda x: x['thue'], reverse=True)