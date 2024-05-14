# Khởi tạo từ điển chứa thông tin thí sinh
thong_tin_thisinh = {
    12345: {"ho_ten": "Nguyễn Văn A", "diem_thi": 8.5},
    23456: {"ho_ten": "Trần Thị B", "diem_thi": 7.9},
    34567: {"ho_ten": "Phạm Văn C", "diem_thi": 9.2}
}

so_bao_danh_can_tra_cuu = int(input("Nhập số báo danh cần tra cứu: "))

if so_bao_danh_can_tra_cuu in thong_tin_thisinh:
    thong_tin = thong_tin_thisinh[so_bao_danh_can_tra_cuu]
    ho_ten = thong_tin["ho_ten"]
    diem_thi = thong_tin["diem_thi"]
    print(f"Thí sinh có số báo danh {so_bao_danh_can_tra_cuu} là {ho_ten} và có điểm thi là {diem_thi}")
else:
    ho_ten = input("Nhập họ và tên của thí sinh: ")
    diem_thi = float(input("Nhập điểm thi của thí sinh: "))
    thong_tin_thisinh[so_bao_danh_can_tra_cuu] = {"ho_ten": ho_ten, "diem_thi": diem_thi}
    print(f"Đã thêm thông tin của thí sinh có số báo danh {so_bao_danh_can_tra_cuu}")
print(thong_tin_thisinh)