print("Nhập nhật ký giao dịch (D là tiền gửi, W là tiền rút ra):")
nhat_ky_giao_dich = []
while True:
    nhap = input("Nhập giao dịch (hoặc nhấn Enter để kết thúc): ")
    if nhap:
        nhat_ky_giao_dich.append(nhap)
    else:
        break
so_tien_thuc = 0
for giao_dich in nhat_ky_giao_dich:
    loai, so_tien = giao_dich.split()
    if loai == 'D':
        so_tien_thuc += int(so_tien)
    elif loai == 'W':
        so_tien_thuc -= int(so_tien)
print("Số tiền thực của tài khoản ngân hàng là:", so_tien_thuc)
