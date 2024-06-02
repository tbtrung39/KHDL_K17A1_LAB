import os
import csv

def tinh_luong(he_so_luong):
    return he_so_luong * 1490000

def tinh_phu_cap(chuc_vu):
    if chuc_vu == "TP":
        return 1000000
    elif chuc_vu == "PP":
        return 700000
    elif chuc_vu == "NV":
        return 300000
    return 0

def tinh_thuc_linh(luong, phu_cap):
    return luong + phu_cap

def nhap_nhan_vien():
    ma_nv = input("Nhap ma NV: ")
    ten_nv = input("Nhap ten NV: ")
    chuc_vu = input("Nhap chuc vu (TP/PP/NV): ")
    he_so_luong = float(input("Nhap he so luong: "))
    luong = tinh_luong(he_so_luong)
    phu_cap = tinh_phu_cap(chuc_vu)
    thuc_linh = tinh_thuc_linh(luong, phu_cap)
    return {
        "Ma NV": ma_nv,
        "Ten NV": ten_nv,
        "Chuc Vu": chuc_vu,
        "He So Luong": he_so_luong,
        "Luong": luong,
        "Phu Cap": phu_cap,
        "Thuc Linh": thuc_linh
    }

def ghi_ds_nhan_vien(ds_nhan_vien, filename):
    keys = ds_nhan_vien[0].keys()
    with open(filename, 'w', newline='') as file:
        dict_writer = csv.DictWriter(file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(ds_nhan_vien)

def main():
    ds_nhan_vien = []
    while True:
        nv = nhap_nhan_vien()
        ds_nhan_vien.append(nv)
        tiep_tuc = input("Nhap tiep? (y/n): ")
        if tiep_tuc.lower() != 'y':
            break

    # Đường dẫn thư mục 8
    directory = '8'
    
    # Tạo thư mục nếu chưa tồn tại
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Tạo đường dẫn đầy đủ cho file ds_nhanvien.csv
    filepath = os.path.join(directory, 'ds_nhanvien.csv')

    ghi_ds_nhan_vien(ds_nhan_vien, filepath)
    print(f"File da duoc luu tai: {filepath}")

if __name__ == "__main__":
    main()
