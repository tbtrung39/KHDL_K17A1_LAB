def nhap_thong_tin_hang_hoa():
    """Nhập thông tin các mặt hàng từ bàn phím"""
    ds_hang_hoa = []
    while True:
        ma_hang = input("Nhập mã hàng (4 ký tự, để kết thúc nhập nhấn Enter): ")
        if not ma_hang:
            break
        if len(ma_hang) != 4:
            print("Mã hàng phải có đúng 4 ký tự.")
            continue
        ten_hang = input("Nhập tên hàng: ")
        don_vi_tinh = input("Nhập đơn vị tính: ")
        try:
            don_gia = float(input("Nhập đơn giá: "))
            so_luong = int(input("Nhập số lượng: "))
        except ValueError:
            print("Đơn giá phải là số thực và số lượng phải là số nguyên.")
            continue

        hang_hoa = {
            'ma_hang': ma_hang,
            'ten_hang': ten_hang,
            'don_vi_tinh': don_vi_tinh,
            'don_gia': don_gia,
            'so_luong': so_luong,
            'thanh_tien': 0,
            'thue_vat': 0
        }
        ds_hang_hoa.append(hang_hoa)
    return ds_hang_hoa

def tinh_thanh_tien(ds_hang_hoa):
    """Tính cột thành tiền với thành tiền = đơn giá * số lượng"""
    for hang_hoa in ds_hang_hoa:
        hang_hoa['thanh_tien'] = hang_hoa['don_gia'] * hang_hoa['so_luong']

def tinh_thue_vat(ds_hang_hoa):
    """Tính cột Thuế với Thuế = thành tiền * 10%"""
    for hang_hoa in ds_hang_hoa:
        hang_hoa['thue_vat'] = hang_hoa['thanh_tien'] * 0.1

def sap_xep_theo_thue(ds_hang_hoa):
    """Sắp xếp các mặt hàng theo thứ tự giảm dần về Thuế"""
    return sorted(ds_hang_hoa, key=lambda x: x['thue_vat'], reverse=True)
