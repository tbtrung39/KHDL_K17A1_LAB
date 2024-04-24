# Tạo một từ điển để lưu thông tin của các thí sinh
thi_sinh = {
    123: {"ho_ten": "Nguyen Van A", "diem_thi": 8.5},
    456: {"ho_ten": "Tran Thi B", "diem_thi": 7.2},
    789: {"ho_ten": "Le Van C", "diem_thi": 9.0}
}

# Nhập số báo danh để tra cứu
so_bao_danh = int(input("Nhập số báo danh của thí sinh: "))

if so_bao_danh in thi_sinh:
    thong_tin = thi_sinh[so_bao_danh]
    print(f"Họ và tên: {thong_tin['ho_ten']}")
    print(f"Điểm thi: {thong_tin['diem_thi']}")
else:
    ho_ten = input("Nhập họ và tên của thí sinh: ")
    diem_thi = float(input("Nhập điểm thi của thí sinh: "))
    thi_sinh[so_bao_danh] = {"ho_ten": ho_ten, "diem_thi": diem_thi}
    print("Thông tin thí sinh đã được bổ sung.")