def nhap_thong_tin_hang_hoa():
    hang_hoa = []
    while True:
        ma_hang = input("Nhập mã hàng (4 ký tự): ")
        ten_hang = input("Nhập tên hàng: ")
        don_vi_tinh = input("Nhập đơn vị tính: ")
        don_gia = float(input("Nhập đơn giá: "))
        so_luong = int(input("Nhập số lượng: "))
        thanh_tien = don_gia * so_luong
        thue_vat = thanh_tien * 0.1
        
        hang_hoa.append({
            'ma_hang': ma_hang,
            'ten_hang': ten_hang,
            'don_vi_tinh': don_vi_tinh,
            'don_gia': don_gia,
            'so_luong': so_luong,
            'thanh_tien': thanh_tien,
            'thue_vat': thue_vat
        })
        
        tiep_tuc = input("Bạn có muốn nhập thêm hàng hóa không? (C/K): ")
        if tiep_tuc.upper() != 'C':
            break
    
    return hang_hoa

def sap_xep_theo_thue(hang_hoa):
    hang_hoa_sau_sap_xep = sorted(hang_hoa, key=lambda x: x['thue_vat'], reverse=True)
    return hang_hoa_sau_sap_xep

def in_hang_hoa(hang_hoa):
    print("Danh sách hàng hóa:")
    for hang in hang_hoa:
        print("Mã hàng:", hang['ma_hang'])
        print("Tên hàng:", hang['ten_hang'])
        print("Đơn vị tính:", hang['don_vi_tinh'])
        print("Đơn giá:", hang['don_gia'])
        print("Số lượng:", hang['so_luong'])
        print("Thành tiền:", hang['thanh_tien'])
        print("Thuế VAT:", hang['thue_vat'])
        print()
