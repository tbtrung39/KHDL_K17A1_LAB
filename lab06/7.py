#7A
danh_sach_goc=[["mom",73],["tue",89],["wed",95],["thu",103],["fri",115],["sat",128],["sun",120]]
print(danh_sach_goc)
for item in danh_sach_goc:
    print(item)
danh_sach_moi=list(danh_sach_goc)
#in ra
print(danh_sach_moi)
for item in danh_sach_moi:
    print(item)
#7b
for sublist in danh_sach_goc:
    if len(sublist)>=3:
        phan_tu=sublist[2]
        print("phan tu thuoc vi tri thu ba",phan_tu)
    else:
        print("phan tu khong thuoc vi ri thu ba")
#7c 
# kiem tra do dai
import random
print("do dai truoc khi them la:",len(danh_sach_goc))
# them danh sach moi
sublist_moi=["ngay mai",random.randint(50,150)]
#them vao danh sach goc
danh_sach_goc.append(sublist_moi)
print("dannh sach goc sau khi duoc them la",danh_sach_goc)
# tinhs sale valur
sale_value=0
for sublist in danh_sach_goc:
    if sublist[0] in ["thu hai","thu ba","thu thu bay","chu nhat"]:
        sale_value+=sublist[1]
print(sale_value)