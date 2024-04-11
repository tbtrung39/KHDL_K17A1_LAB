nhat_ky_giao_dich = []

while True:
    giao_dich = input("Nhập giao dịch (D/W/X để kết thúc): ").strip().upper()
    if giao_dich == 'X':
        break
    else:
        nhat_ky_giao_dich.append(giao_dich)

so_tien = 0
for giao_dich in nhat_ky_giao_dich:
    loai, so = giao_dich[0], float(giao_dich[1:])
    if loai == 'D':
        so_tien += so
    elif loai == 'W':
        so_tien -= so

print("Số tiền thực của tài khoản:", so_tien)