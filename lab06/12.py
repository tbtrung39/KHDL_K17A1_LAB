lich_su=[]
while True:
    giao_dich=input().strip()
    print("Nhập lịch sử giao dịch(nhap finish để dừng):")
    if giao_dich=="finish":
        break
    lich_su.append(giao_dich)

so_tien_thuc=0
for i in lich_su:
    loai_giao_dich,so_tien=giao_dich.split()
    if loai_giao_dich=="D":
        so_tien_thuc+=so_tien
    elif loai_giao_dich=="W":
        so_tien_thuc-=so_tien
print("Số tiền trong tài khoản:",so_tien_thuc)