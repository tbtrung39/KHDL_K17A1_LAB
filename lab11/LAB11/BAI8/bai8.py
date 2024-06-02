import os
import csv

class NhanVien:
    def __init__(self, ma_nv, ten_nv, chuc_vu, he_so_luong):
        self.ma_nv = ma_nv
        self.ten_nv = ten_nv
        self.chuc_vu = chuc_vu
        self.he_so_luong = he_so_luong
        self.luong = self.tinh_luong()
        self.phu_cap = self.tinh_phu_cap()
        self.thuc_linh = self.tinh_thuc_linh()

    def tinh_luong(self):
        return self.he_so_luong * 1490000

    def tinh_phu_cap(self):
        if self.chuc_vu == "TP":
            return 1000000
        elif self.chuc_vu == "PP":
            return 700000
        elif self.chuc_vu == "NV":
            return 300000
        return 0

    def tinh_thuc_linh(self):
        return self.luong + self.phu_cap

    def to_dict(self):
        return {
            "Ma NV": self.ma_nv,
            "Ten NV": self.ten_nv,
            "Chuc Vu": self.chuc_vu,
            "He So Luong": self.he_so_luong,
            "Luong": self.luong,
            "Phu Cap": self.phu_cap,
            "Thuc Linh": self.thuc_linh
        }

def nhap_nhan_vien():
    ma_nv = input("Nhap ma NV: ")
    ten_nv = input("Nhap ten NV: ")
    chuc_vu = input("Nhap chuc vu (TP/PP/NV): ")
    he_so_luong = float(input("Nhap he so luong: "))
    return NhanVien(ma_nv, ten_nv, chuc_vu, he_so_luong)

def ghi_ds_nhan_vien(ds_nhan_vien, filename):
    keys = ds_nhan_vien[0].to_dict().keys()
    with open(filename, 'w', newline='') as file:
        dict_writer = csv.DictWriter(file, keys)
        dict_writer.writeheader()
        dict_writer.writerows([nv.to_dict() for nv in ds_nhan_vien])

def main():
    ds_nhan_vien = []
    while True:
        nv = nhap_nhan_vien()
        ds_nhan_vien.append(nv)
        tiep_tuc = input("Nhap tiep? (y/n): ")
        if tiep_tuc.lower() != 'y':
            break

    # Đường dẫn thư mục BAI8
    directory = 'BAI8'
    
    # Tạo thư mục nếu chưa tồn tại
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Tạo đường dẫn đầy đủ cho file ds_nhanvien.csv
    filepath = os.path.join(directory, 'ds_nhanvien.csv')

    ghi_ds_nhan_vien(ds_nhan_vien, filepath)
    print(f"File da duoc luu tai: {filepath}")

if __name__ == "__main__":
    main()
