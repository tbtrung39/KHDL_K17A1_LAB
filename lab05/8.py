van_ban=input("Nhap van ban:")
tim_kiem=input("Nhap tu can tim:")
tu_don=van_ban.split()
danh_sach=[]
for i in tu_don:
    if i==tim_kiem:
        danh_sach.append(i)
print("Tu",tim_kiem,"xuat hien trong van_ban",len(danh_sach),"lan")