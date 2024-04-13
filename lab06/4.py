danh_sach=[]
while True:
    phan_tu=int(input("moi nhap phan tu"))
    danh_sach.append(phan_tu)
    if phan_tu==0:
        print("ket thuc chuong trinh")
        break
danh_sach_moi=[1,2,3]
# chen danh vao vi tri dau
danh_sach.insert(0,danh_sach_moi)
# chen danh sach vao vi tri thu 5
danh_sach.insert(4,danh_sach_moi)
# chen vao cuoi
danh_sach.append(danh_sach_moi)
print("cac vi tri ma danh sach moi duoc nhap vao la:",danh_sach)
# xoa bo phan tu k
k=int(input("nhap he so k"))
if k in danh_sach:
    danh_sach.remove(k)
    print("k da duoc xoa khoi dnah sach")
else:
    print("k chua duoc xoa khoi danh sach")
# sap xeo
# sap xep tang adan\
danh_sach_tang_dan=sorted(danh_sach)
print("dnah sach tang dan la:",danh_sach_tang_dan)
# sap xep danh sahc giam
danh_sach_giam_dan=sorted(danh_sach, reverse=True)
print("danh sach giam dan la:",danh_sach_giam_dan)