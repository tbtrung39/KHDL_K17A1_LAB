n = int(input("Nhap so phan tu danh sach la:"))
danh_sach = []
for i in range(n):
    phan_tu = int(input(f"Nhap phan tu thu {i+1}:"))
    danh_sach.append(phan_tu)
print(danh_sach)

ds_moi = sorted(danh_sach,reverse=True)
b = ds_moi[1]
print(f"Phan tu lon thu 2 la {ds_moi[1]}")
print(f"Vi tri cua phan tu lon thu 2 la: {danh_sach.index(b)}")

dem = 0
max_dem = 0
tong = 0
max_tong = 0
for i in danh_sach:
    if i > 0:
        dem += 1
        tong += i
        max_dem = max(max_dem,dem)
        max_tong = max(max_tong,tong)
    else:
        dem = 0
        tong = 0
print("So luong cac so duong nhieu nhat la:",max_dem)
print("Tong cac so duong lien tiep la:",max_tong)