n=int(input("nhap vao so phan tu: "))
lst=[]
for i in range(0,n):
    phan_tu=int(input("nhap so tu nhien:"))
    lst.append(phan_tu)
print('danh sach:', lst)

lst.sort(reverse=True)
lon_thu_hai=lst[1]
vi_tri_lon_thu_hai=lst.index(lon_thu_hai)
print("phan tu lon thu 2 la:", lon_thu_hai)
print("vi tri phan tu lon thu 2 la:", vi_tri_lon_thu_hai)

so_duong_lien_tiep_max=0
so_duong_lien_tiep_hien_tai=0
for i in lst:
    if i >0:
        so_duong_lien_tiep_max+=1
        if so_duong_lien_tiep_hien_tai>so_duong_lien_tiep_max:
            so_duong_lien_tiep_max=so_duong_lien_tiep_hien_tai
        else:
            so_duong_lien_tiep_hien_tai=0
print("so luong so duong lien tiep nhieu nhat la:", so_duong_lien_tiep_hien_tai)

tong_max=0
tong_hien_tai=0
so_luong_lien_tiep=0
for i in lst:
    if i>0:
        so_luong_lien_tiep+=1
        tong_hien_tai+=i
        if tong_hien_tai>tong_max:
            tong_max=tong_hien_tai
    else:
        so_luong_lien_tiep=0
        tong_hien_tai=0
print("tong so duong lien tiep co tong lon nhat la:", tong_max)