lich_su=[]
print("nhap lich su gioa dich (nhap'done' de tong ket thuc):")
while True:
    giao_dich= input().strip()
    if giao_dich.lower()=='done':
        break
    lich_su.append(giao_dich)

so_tien_thuc=0
for i in lich_su:
    loai_giao_dich, so_tien = giao_dich.split()
    if loai_giao_dich=='D':
        so_tien_thuc+= int(so_tien)
    elif loai_giao_dich =='W':
        so_tien_thuc-=int(so_tien)
print("so tien thuc trong tai khoan ngan hang cua ban la ",so_tien_thuc)
