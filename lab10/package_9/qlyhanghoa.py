# Module: qlyhanghoa.py

class MatHang:
    def __init__(self, ma_hang, ten_hang, don_vi_tinh, don_gia, so_luong):
        self.ma_hang = ma_hang
        self.ten_hang = ten_hang
        self.don_vi_tinh = don_vi_tinh
        self.don_gia = don_gia
        self.so_luong = so_luong
        self.thanh_tien = self.tinh_thanh_tien()
        self.thue_vat = self.tinh_thue_vat()

    def tinh_thanh_tien(self):
        return self.don_gia * self.so_luong

    def tinh_thue_vat(self):
        return self.thanh_tien * 0.1

    def hien_thi(self):
        return f"{self.ma_hang}\t{self.ten_hang}\t{self.don_vi_tinh}\t{self.don_gia}\t{self.so_luong}\t{self.thanh_tien}\t{self.thue_vat}"

def nhap_thong_tin_mat_hang():
    ma_hang = input("Nhập mã hàng (4 ký tự): ")
    ten_hang = input("Nhập tên hàng: ")
    don_vi_tinh = input("Nhập đơn vị tính: ")
    don_gia = float(input("Nhập đơn giá: "))
    so_luong = int(input("Nhập số lượng: "))
    return MatHang(ma_hang, ten_hang, don_vi_tinh, don_gia, so_luong)

def nhap_danh_sach_mat_hang():
    danh_sach = []
    so_mat_hang = int(input("Nhập số lượng mặt hàng: "))
    for _ in range(so_mat_hang):
        mat_hang = nhap_thong_tin_mat_hang()
        danh_sach.append(mat_hang)
    return danh_sach

def sap_xep_giam_dan_theo_thue(danh_sach):
    return sorted(danh_sach, key=lambda mh: mh.thue_vat, reverse=True)

def hien_thi_danh_sach(danh_sach):
    print("Mã hàng\tTên hàng\tĐơn vị tính\tĐơn giá\tSố lượng\tThành tiền\tThuế VAT")
    for mh in danh_sach:
        print(mh.hien_thi())