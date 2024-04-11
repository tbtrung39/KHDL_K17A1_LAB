# Nhập nhật ký giao dịch từ người dùng
nhat_ky = input("Nhập nhật ký giao dịch (định dạng D/W số_tiền): ").split()

so_tien_thuc = 0
for i in range(0, len(nhat_ky), 2):
    if nhat_ky[i] == 'D':
        so_tien_thuc += int(nhat_ky[i+1])
    elif nhat_ky[i] == 'W':
        so_tien_thuc -= int(nhat_ky[i+1])

print("Số tiền thực của tài khoản ngân hàng là:", so_tien_thuc)
