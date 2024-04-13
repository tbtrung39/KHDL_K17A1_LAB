nhat_ky = []
print("Nhập nhật ký giao dịch:")
while True:
    giao_dich = input().split()
    if not giao_dich:
        break
    nhat_ky.append(giao_dich)

so_tien_thuc = sum(int(so_tien) if loai == 'D' else -int(so_tien) for loai, so_tien in nhat_ky)

print("Số tiền thực của tài khoản là:", so_tien_thuc)