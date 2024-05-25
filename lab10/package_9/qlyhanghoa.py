def nhap_mat_hang():
    ma_hang = input("nhap ma hang (4 ký tự): ")
    ten_hang = input("nhap ten hang: ")
    don_vi_tinh = input("nhap don vi tinh: ")
    don_gia = float(input("nhap don gia: "))
    so_luong = int(input("nhap so luong: "))
    thanh_tien = don_gia * so_luong
    thue = thanh_tien * 0.1
    return {
        "ma_hang": ma_hang,
        "ten_hang": ten_hang,
        "don_vi_tinh": don_vi_tinh,
        "don_gia": don_gia,
        "so_luong": so_luong,
        "thanh_tien": thanh_tien,
        "thue": thue}

def sap_xep_theo_thue(danh_sach_mat_hang):
    danh_sach_mat_hang.sort(key=lambda mat_hang: mat_hang["thue"], reverse=True)

def hien_thi_danh_sach_mat_hang(danh_sach_mat_hang):
    print("Danh sach hang sau khi sap xep:")
    for mat_hang in danh_sach_mat_hang:
        print("ma hang:", mat_hang["ma_hang"])
        print("ten hang:", mat_hang["ten_hang"])
        print("don vi tinh:", mat_hang["don_vi_tinh"])
        print("don gia:", mat_hang["don_gia"])
        print("so luong:", mat_hang["so_luong"])
        print("thanh tien:", mat_hang["thanh_tien"])
        print("thue:", mat_hang["thue"])
        print()