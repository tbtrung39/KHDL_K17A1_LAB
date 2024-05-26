def nhap_thong_tin_hang_hoa():
    danh_sach_hang_hoa = []
    so_luong_hang = int(input("Nhập số lượng mặt hàng: "))
    for _ in range(so_luong_hang):
        ma_hang = input("Nhập mã hàng (4 ký tự): ")
        ten_hang = input("Nhập tên hàng: ")
        don_vi_tinh = input("Nhập đơn vị tính: ")
        don_gia = float(input("Nhập đơn giá: "))
        so_luong = int(input("Nhập số lượng: "))
        mat_hang = {
            'ma_hang': ma_hang,
            'ten_hang': ten_hang,
            'don_vi_tinh': don_vi_tinh,
            'don_gia': don_gia,
            'so_luong': so_luong,
            'thanh_tien': 0,
            'thue': 0
        }
        danh_sach_hang_hoa.append(mat_hang)
    return danh_sach_hang_hoa

def tinh_thanh_tien(danh_sach_hang_hoa):
    for hang in danh_sach_hang_hoa:
        hang['thanh_tien'] = hang['don_gia'] * hang['so_luong']

def tinh_thue(danh_sach_hang_hoa):
    for hang in danh_sach_hang_hoa:
        hang['thue'] = hang['thanh_tien'] * 0.10

def sap_xep_theo_thue(danh_sach_hang_hoa):
    danh_sach_hang_hoa.sort(key=lambda x: x['thue'], reverse=True)

def hien_thi_hang_hoa(danh_sach_hang_hoa):
    print(f"{'Mã hàng':<10}{'Tên hàng':<20}{'Đơn vị tính':<15}{'Đơn giá':<10}{'Số lượng':<10}{'Thành tiền':<15}{'Thuế':<10}")
    for hang in danh_sach_hang_hoa:
        print(f"{hang['ma_hang']:<10}{hang['ten_hang']:<20}{hang['don_vi_tinh']:<15}{hang['don_gia']:<10}{hang['so_luong']:<10}{hang['thanh_tien']:<15}{hang['thue']:<10}")
