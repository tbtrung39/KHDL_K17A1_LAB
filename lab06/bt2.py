n = int(input("Số phần tử danh sách: "))
danh_sach = []
for i in range(n):
    phan_tu = int(input(f"Nhập phần tử thứ {i+1}: "))
    danh_sach.append(phan_tu)
print(danh_sach)
danh_sach_sap_xep = sorted(danh_sach)
phan_tu_lon_thu_2 = danh_sach_sap_xep[-2]
vi_tri = danh_sach.index(phan_tu_lon_thu_2) 
print("Phần tử lớn thứ 2 danh sách: ", phan_tu_lon_thu_2)
print("Vị trí của phần tử lớn thứ 2: ", vi_tri)

so_luong_so_duong_lien_tiep = 0
so_luong_so_duong_hien_tai = 0
for so in danh_sach:
    if so > 0:
        so_luong_so_duong_hien_tai += 1
        if so_luong_so_duong_hien_tai > so_luong_so_duong_lien_tiep:
            so_luong_so_duong_lien_tiep = so_luong_so_duong_hien_tai
    else:
        so_luong_so_duong_hien_tai = 0
print("Số lượng các số dương liên tiếp nhiều nhất:", so_luong_so_duong_lien_tiep)