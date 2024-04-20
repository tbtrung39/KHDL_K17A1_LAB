# thong ke chieu cao
# nhom co so luong sinh vien 
chieu_cao=[161, 182, 161, 154, 176, 170, 167, 171, 170, 174, 150, 142, 148, 165, 170, 178, 156, 145, 149, 163,
           162, 159, 165, 165, 170, 180 ,155, 159, 155, 153, 152, 162, 180, 168, 169, 168, 167, 170] 
so_lan_xuat_hien={}
for chieu_cao in chieu_cao:
    if chieu_cao in so_lan_xuat_hien:
        so_lan_xuat_hien[chieu_cao]+=1
    else:
        so_lan_xuat_hien[chieu_cao]=1
tong_so_sinh_vien=sum(so_lan_xuat_hien.values())
print("nhom co so luong sinh vien la:",tong_so_sinh_vien)

# chieu cao trung binh cua cac sinh vien trong nhom
chieu_cao=[161, 182, 161, 154, 176, 170, 167, 171, 170, 174, 150, 142, 148, 165, 170, 178, 156, 145, 149, 163,
           162, 159, 165, 165, 170, 180 ,155, 159, 155, 153, 152, 162, 180, 168, 169, 168, 167, 170] 
chieu_cao_trung_binh=sum(chieu_cao)/len(chieu_cao)
print("chieu cao trung binh cua nhom hoc sinh la:",chieu_cao_trung_binh)

# liet ke cac chieu cao khac nhau va tinh 
# kiet ke
chieu_cao_khac_nhau=set(chieu_cao)
print("co nhung chieu cao khac nhau la",chieu_cao_khac_nhau)
# tinh chieu cao trung binh
chieu_cao_trung_binh=sum[chieu_cao]/len[chieu_cao]
print("chieu cao trung binh la:",chieu_cao_trung_binh)