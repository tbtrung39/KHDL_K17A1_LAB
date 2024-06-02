import csv
import os
def tinh_diemtl(diemtb, diemrl):
    return (diemtb+diemrl)/2

def nhap_thong_tin_sv():
    ma_sv = input("Nhập mã sv: ")
    ten = input("Nhập tên sv: ")
    diemtb= float(input("Nhập điem: "))
    diemrl= float(input("Nhập điem: "))

def luu_danh_sv(file_name, danh_sachsv):
    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(danh_sachsv)

def sap_xep(danh_sachsv):
    danh_sach_da_sap_xep = sorted(danh_sachsv, key=lambda x: x[4], reverse=True)
    return danh_sach_da_sap_xep


def in_danh_sachsv(danh_sachsv):
    for sv in danh_sachsv:
        print(sv)

def mo_file_dssv(file_name):
    try:
        with open(file_name, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("File không tồn tại.")

def main():
    nfo_file = "files/ds_sv.csv"
    with open("files/ds_sv.csv", 'w', encoding="utf-8-sig") as f:
        f.write("1234,Nguyễn Văn A,điểm tb 8,điểm rl 85")
        f.write("1254,Lê Thị C,điẻm tb 7,diem rl 65,\n")
        f.write("3245,Lê Thị D,điểmtb 6, diem rl 76\n")

    while True:
        print("\n===== MENU =====")
        print("1. Nhập thông tin sv")
        print("2. Mở file danh sách sv")
        print("3. Tính diem tl")
        print("4. Lưu danh sách và sắp xếp")
        print("5. Thoát")

        choice = input("Chọn chức năng (1-5): ")
        
   