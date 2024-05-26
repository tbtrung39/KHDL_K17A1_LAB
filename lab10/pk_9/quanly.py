def nhap_thong_tin_hang_hoa():
    hang_hoa = []
    while True:
        ma_hang = input("Nhập mã hàng (4 kí tự): ")
        ten_hang = input("Nhập tên hàng: ")
        don_vi_tinh = input("Nhập đơn vị tính: ")
        don_gia = float(input("Nhập đơn giá: "))
        so_luong = int(input("Nhập số lượng: "))
        thanh_tien = don_gia * so_luong
        thue_VAT = thanh_tien * 0.1
        hang_hoa.append((ma_hang, ten_hang, don_vi_tinh, don_gia, so_luong, thanh_tien, thue_VAT))
        tiep_tuc = input("Bạn có muốn nhập tiếp không? (c/k): ")
        if tiep_tuc.lower() != 'c':
            break
    return hang_hoa

def tinh_thanh_tien(hang_hoa):

    for i in range(len(hang_hoa)):
        hang_hoa[i] = (*hang_hoa[i][:5], hang_hoa[i][3] * hang_hoa[i][4], *hang_hoa[i][5:])

def tinh_thue_VAT(hang_hoa):
    for i in range(len(hang_hoa)):
        hang_hoa[i] = (*hang_hoa[i][:6], hang_hoa[i][5] * 0.1)

def sap_xep_giam_gian(hang_hoa):
    print("Danh sách mặt hàng trước khi sắp xếp:")
    hien_thi_danh_sach_hang_hoa(hang_hoa)

    hang_hoa.sort(key=lambda x: x[6], reverse=True)

    print("\nDanh sách mặt hàng sau khi sắp xếp:")
    hien_thi_danh_sach_hang_hoa(hang_hoa)

def hien_thi_danh_sach_hang_hoa(hang_hoa):
    print("{:<10} {:<20} {:<15} {:<10} {:<10} {:<15} {:<10}".format("Mã hàng", "Tên hàng", "Đơn vị tính", "Đơn giá", "Số lượng", "Thành tiền", "Thuế VAT"))
    for hang in hang_hoa:
        print("{:<10} {:<20} {:<15} {:<10.2f} {:<10} {:<15.2f} {:<10.2f}".format(*hang))
