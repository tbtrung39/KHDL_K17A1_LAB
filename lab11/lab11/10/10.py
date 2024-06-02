import os
import csv

def tinh_diem_tl(diem_tb, diem_rl):
    return (diem_tb + diem_rl) / 2

def nhap_sinh_vien():
    ma_sv = input("Nhap ma SV: ")
    ho_ten = input("Nhap ho ten: ")
    diem_tb = float(input("Nhap diem TB: "))
    diem_rl = float(input("Nhap diem RL: "))
    diem_tl = tinh_diem_tl(diem_tb, diem_rl)
    return {
        "Ma SV": ma_sv,
        "Ho Ten": ho_ten,
        "Diem TB": diem_tb,
        "Diem RL": diem_rl,
        "Diem TL": diem_tl
    }

def ghi_ds_sinh_vien(ds_sinh_vien, filename):
    keys = ds_sinh_vien[0].keys()
    with open(filename, 'w', newline='') as file:
        dict_writer = csv.DictWriter(file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(ds_sinh_vien)

def main():
    ds_sinh_vien = []
    while True:
        sv = nhap_sinh_vien()
        ds_sinh_vien.append(sv)
        tiep_tuc = input("Nhap tiep? (y/n): ")
        if tiep_tuc.lower() != 'y':
            break
    directory = os.getcwd()  # Đường dẫn hiện tại
    filepath = os.path.join(directory, '10', 'sinhvien.csv')  # Tạo đường dẫn đến tệp CSV
    os.makedirs(os.path.dirname(filepath), exist_ok=True)  # Tạo thư mục nếu chưa tồn tại
    ghi_ds_sinh_vien(ds_sinh_vien, filepath)  # Truyền biến filepath, không phải chuỗi 'filepath'

if __name__ == "__main__":
    main()
