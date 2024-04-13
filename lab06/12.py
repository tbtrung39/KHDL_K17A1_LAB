# Nhập chuỗi chứa các giao dịch từ người dùng
giao_dich = input("Nhập chuỗi giao dịch (d: tiền gửi, w: tiền rút ra), cách nhau bằng dấu cách: ")

# Tách chuỗi thành các giao dịch
danh_sach_giao_dich = giao_dich.split()

# Khởi tạo biến để lưu số tiền hiện có
so_tien_hien_co = 0

# Duyệt qua từng giao dịch và cập nhật số tiền hiện có
for giao_dich in danh_sach_giao_dich:
    if giao_dich[0] == 'd':
        so_tien_hien_co += int(giao_dich[1:])
    elif giao_dich[0] == 'w':
        so_tien_hien_co -= int(giao_dich[1:])

# In số tiền hiện có ra màn hình
print("Số tiền hiện có sau các giao dịch là:", so_tien_hien_co)