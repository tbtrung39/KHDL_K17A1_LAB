n = int(input("So phan tu danh sach: "))
danh_sach = []
for i in range(n):
    phan_tu = int(input("Nhap phan tu thu {i+1}: "))
    danh_sach.append(phan_tu)
print(danh_sach)
danh_sach_sap_xep = sorted(danh_sach)
phan_tu_lon_thu_2 = danh_sach_sap_xep[-2]
vi_tri = danh_sach.index(phan_tu_lon_thu_2)
print("Phan tu lon thu 2 danh sach: ", phan_tu_lon_thu_2)
print("Vi tri cua phan tu lon thu 2: ", vi_tri)

cac_so_duong = [x for x in danh_sach_sap_xep if x > 0]
so_luong_cac_so_duong = len(cac_so_duong)
print("So luong cac soduong lien tiep nhieu nhat: ", so_luong_cac_so_duong)