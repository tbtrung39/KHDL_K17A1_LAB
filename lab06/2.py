#Tim ptu lon thu 2 va tim vi tri cua phan tu lon thu hai
danh_sach=[]
while True:
    n = input("nhap sp luong phan tu cua danh sach(nhap f de dung):")
    if n == "f":
        break
    danh_sach.append(n)
print(danh_sach)
#vi_tri_ptu_lon_thu2 = ptu_lon_thu2.index(danh_sach)
list_a= danh_sach.copy()
max1=max(list_a)
list_a.remove(max1)
max2=max(list_a)
vi_tri_ptu_lon_thu2 = danh_sach.index(max2)
print(" phan tu lon thu 2 la ", max2)
print(" vi tri phan tu lon thu 2 la ", vi_tri_ptu_lon_thu2)