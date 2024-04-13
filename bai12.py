print("Nhập nhật ký giao dịch (D là tiền gửi, W là tiền rút ra). Kết thúc bằng Enter:")
nhap_nhat_ky = []
while True:
    nhap = input().strip()
    if not nhap:
        break
    nhap_nhat_ky.append(nhap.split())
so_tien_thuc = sum([int(so_tien) if loai_giao_dich == 'D' else -int(so_tien) for loai_giao_dich, so_tien in nhap_nhat_ky])
print("Số tiền thực của tài khoản ngân hàng là:", so_tien_thuc)