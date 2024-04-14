#12

print("Nhập nhật ký giao dịch (kết thúc bằng nhập 'done'):")
nhat_ky = []
while True:
    giao_dich = input().strip()
    if giao_dich == 'done':
        break
    nhat_ky.append(giao_dich)
so_tien_thuc = 0
for giao_dich in nhat_ky:
    loai_giao_dich, so_tien = giao_dich.split()
    if loai_giao_dich == 'D':
        so_tien_thuc += int(so_tien)
    elif loai_giao_dich == 'W':
        so_tien_thuc -= int(so_tien)
print("Số tiền thực của tài khoản ngân hàng là:", so_tien_thuc)