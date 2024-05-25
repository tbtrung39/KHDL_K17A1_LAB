def nhap_thong_tin():
    danh_sach_hang_hoa = []
    while True:
        ma_hang = input("Nhập mã hàng (4 ký tự): ")
        if len(ma_hang) != 4:
            print("Mã hàng phải có 4 ký tự. Vui lòng nhập lại.")
            continue
        ten_hang = input("Nhập tên hàng: ")
        don_vi_tinh = input("Nhập đơn vị tính: ")
        don_gia = float(input("Nhập đơn giá: "))
        so_luong = float(input("Nhập số lượng: "))
        thanh_tien = don_gia * so_luong
        thue_vat = thanh_tien * 0.1
        hang_hoa = {
            "ma_hang": ma_hang,
            "ten_hang": ten_hang,
            "don_vi_tinh": don_vi_tinh,
            "don_gia": don_gia,
            "so_luong": so_luong,
            "thanh_tien": thanh_tien,
            "thue_vat": thue_vat
        }
        danh_sach_hang_hoa.append(hang_hoa)
        them_nua = input("Bạn có muốn nhập thêm hàng hóa không? (y/n) ")
        if them_nua.lower() != "y":
            break
    return danh_sach_hang_hoa

def sap_xep_giam_dan_thue_vat(danh_sach_hang_hoa):
    return sorted(danh_sach_hang_hoa, key=lambda x: x["thue_vat"], reverse=True)
