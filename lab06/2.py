#2
n=int(input("moi nhap he so n:"))
danh_sach=[]
for i in range(n):
    phan_tu=int(input("moi nhap phan tu{i+1}:"))
    danh_sach.append(phan_tu)

# sap xep vi tri thu hai
danh_sach_sap_xep=sorted(danh_sach, reverse=True)
# phan tu lon thu hai
phan_tu_lon_thu_hai=danh_sach_sap_xep[1]
#vi tri
vi_tri=danh_sach.index(phan_tu_lon_thu_hai)
#xuat ra
print("phan tu lon thu hai la:",phan_tu_lon_thu_hai)
print("vi tri cua phan tu lon thu hai la:",vi_tri)

# 2b
max_so_duong=0
so_duong_lien_tiep=0
for so in danh_sach:
    if so>0:
        so_duong_lien_tiep+=1
        max_so_duong=max(max_so_duong,so_duong_lien_tiep)
    else:
        so_duong_lien_tiep=0
print("so luong cac so duong lien tiep nhieu nhat",max_so_duong)
#2c
max_so_duong=0
so_duong_lien_tiep=0
tong_hien_tai=0
tong_max=0
for so in danh_sach:
    if so>0:
        so_duong_lien_tiep+=1
        tong_hien_tai+=so
    if tong_hien_tai>tong_max:
        tong_hien_tai=tong_max
        so_duong_lien_tiep=max_so_duong
    else:
        so_duong_lien_tiep=0
        tong_hien_tai=0
print("so luong cac so duong lien tiep co tong lon nhat:",max_so_duong)