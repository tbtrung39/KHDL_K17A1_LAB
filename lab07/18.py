thong_tin_thi_sinh = {
    12345: {"ho_ten": "Nguyen Van A", "diem_thi": 8.5},
    23456: {"ho_ten": "Tran Thi B", "diem_thi": 7.9},
    34567: {"ho_ten": "Pham Van C", "diem_thi": 9.2}
}
so_bao_danh_can_tra_cuu = int(input("Nhap so bao danh can tra cuu: "))
if so_bao_danh_can_tra_cuu in thong_tin_thi_sinh:
    thong_tin = thong_tin_thi_sinh[so_bao_danh_can_tra_cuu]
    ho_ten = thong_tin["ho_ten"]
    diem_thi = thong_tin["diem_thi"]
    print(f"Thi sinh co so bao danh {so_bao_danh_can_tra_cuu} la {ho_ten} va co diem thi la {diem_thi}")
else:
    ho_ten = input("Nhap ho va ten cua thi sinh: ")
    diem_thi = float(input("Nhap diem thi cua thi sinh: "))
    thong_tin_thi_sinh[so_bao_danh_can_tra_cuu] = {"ho_ten": ho_ten, "diem_thi": diem_thi}
    print(f"Da them thong tin cua thi sinh co so bao danh {so_bao_danh_can_tra_cuu}")
print(thong_tin_thi_sinh)