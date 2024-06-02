import os
import csv

class SinhVien:
    def __init__(self, ma_sv, ho_ten, diem_tb, diem_rl):
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.diem_tb = diem_tb
        self.diem_rl = diem_rl
        self.diem_tl = self.tinh_diem_tl()

    def tinh_diem_tl(self):
        return (self.diem_tb + self.diem_rl) / 2

    def to_dict(self):
        return {
            "Ma SV": self.ma_sv,
            "Ho Ten": self.ho_ten,
            "Diem TB": self.diem_tb,
            "Diem RL": self.diem_rl,
            "Diem TL": self.diem_tl
        }

def nhap_sinh_vien():
    ma_sv = input("Nhap ma SV: ")
    ho_ten = input("Nhap ho ten: ")
    diem_tb = float(input("Nhap diem TB: "))
    diem_rl = float(input("Nhap diem RL: "))
    return SinhVien(ma_sv, ho_ten, diem_tb, diem_rl)

def ghi_ds_sinh_vien(ds_sinh_vien, filename):
    keys = ds_sinh_vien[0].to_dict().keys()
    with open(filename, 'w', newline='') as file:
        dict_writer = csv.DictWriter(file, keys)
        dict_writer.writeheader()
        dict_writer.writerows([sv.to_dict() for sv in ds_sinh_vien])

def main():
    ds_sinh_vien = []
    while True:
        sv = nhap_sinh_vien()
        ds_sinh_vien.append(sv)
        tiep_tuc = input("Nhap tiep? (y/n): ")
        if tiep_tuc.lower() != 'y':
            break
    directory = os.getcwd()  # Đường dẫn hiện tại
    filepath = os.path.join(directory, 'BAI10', 'sinhvien.csv')  # Tạo đường dẫn đến tệp CSV
    ghi_ds_sinh_vien(ds_sinh_vien, filepath)  # Truyền biến filepath, không phải chuỗi 'filepath'

if __name__ == "__main__":
    main()