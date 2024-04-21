# Tạo một từ điển chứa thông tin thí sinh
thong_tin_thisinh = {
    '123456': {'Họ và tên': 'Nguyễn Văn A', 'Điểm thi': 8.5},
    '234567': {'Họ và tên': 'Trần Thị B', 'Điểm thi': 7.0},
    '345678': {'Họ và tên': 'Lê Văn C', 'Điểm thi': 9.25}
}

# Nhập số báo danh để tra c
sobd_can_tra_cuu = input("Nhập số báo danh cần tra cứu: ")

# Tra cứu điểm thi của thí sinh
if sobd_can_tra_cuu in thong_tin_thisinh:
    thong_tin = thong_tin_thisinh[sobd_can_tra_cuu]
    print(f"Thí sinh có số báo danh {sobd_can_tra_cuu} có thông tin như sau:")
    print(f"Họ và tên: {thong_tin['Họ và tên']}")
    print(f"Điểm thi: {thong_tin['Điểm thi']}")
else:
    print("Không tìm thấy thí sinh có số báo danh này.")

# Nếu không tìm thấy thí sinh, thêm thông tin mới
if sobd_can_tra_cuu not in thong_tin_thisinh:
    chon = input("Thí sinh không tồn tại, bạn có muốn thêm thông tin mới không? (C/K): ")
    if chon.lower() == 'c':
        hoten = input("Nhập họ và tên của thí sinh: ")
        diemthi = float(input("Nhập điểm thi của thí sinh: "))
        thong_tin_thisinh[sobd_can_tra_cuu] = {'Họ và tên': hoten, 'Điểm thi': diemthi}
        print("Thêm thông tin thí sinh thành công!")

# In ra danh sách thí sinh sau khi cập nhật
print("\nDanh sách thí sinh sau khi cập nhật:")
for sobd, thong_tin in thong_tin_thisinh.items():
    print(f"Số báo danh: {sobd}, Họ và tên: {thong_tin['Họ và tên']}, Điểm thi: {thong_tin['Điểm thi']}")