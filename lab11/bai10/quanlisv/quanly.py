import csv

def nhap_thong_tin_sinh_vien():
    so_luong_sinh_vien = int(input("Nhập số lượng sinh viên: "))
    danh_sach_sinh_vien = []
    for i in range(1, so_luong_sinh_vien + 1):
        print(f"Nhập thông tin sinh viên thứ {i} là:")
        ma_sinh_vien = input("Nhập mã sinh viên:")
        ten_sinh_vien = input("Nhập tên sinh viên: ")
        diem_trung_binh = float(input("Nhập điểm trung bình: "))
        diem_ren_luyen = float(input("Nhập điểm rèn luyện: "))
        diem_tich_luy = (diem_trung_binh + diem_ren_luyen) / 2
        danh_sach_sinh_vien.append([ma_sinh_vien, ten_sinh_vien, diem_trung_binh, diem_ren_luyen, diem_tich_luy])
    return danh_sach_sinh_vien

def ghi_thong_tin_sinh_vien(danh_sach_sinh_vien):
    with open("lab11/bai10/file/ds_sv", mode="w", newline='') as file_ds:
        ten_cot = ["Mã SV", "Họ Tên", "Điểm TB", "Điểm RL", "Điểm TL"]
        csv.DictWriter(file_ds, fieldnames=ten_cot).writeheader()
        csv.writer(file_ds).writerows(danh_sach_sinh_vien)

def in_thong_tin_sinh_vien(danh_sach_sinh_vien):
    danh_sach_sinh_vien = sorted(danh_sach_sinh_vien, key=lambda x: x[3])
    print("Thông tin sinh viên sau khi sắp xếp tăng dần của điểm rèn luyện là:")
    for sinh_vien in danh_sach_sinh_vien:
        print("{:<10}".format(sinh_vien), end="")
    print()

def tim_sinh_vien_diem_cao_nhat(danh_sach_sinh_vien):
    sinh_vien_diem_cao_nhat = max(danh_sach_sinh_vien, key=lambda x: x[4])
    print(f"Thông tin sinh viên có điểm tích lũy cao nhất là:\n{sinh_vien_diem_cao_nhat}")

# Chương trình chính
danh_sach_sinh_vien = nhap_thong_tin_sinh_vien()
ghi_thong_tin_sinh_vien(danh_sach_sinh_vien)
in_thong_tin_sinh_vien(danh_sach_sinh_vien)
tim_sinh_vien_diem_cao_nhat(danh_sach_sinh_vien)
