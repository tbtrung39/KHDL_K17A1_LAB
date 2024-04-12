a = [2,-4,1,9,-3,6,3,-2,6,8]
s = sum(a)
so_duong = sum([i for i in a if i>=0])
so_am = [i for i in a if i<0]
phan_tu_duong_cuoi = [i for i in a if i>=0]
lon_nhat = max(a)
print("Tong ca phan tu la: ", s)
print("Tong cac so duong la: ", so_duong)
print("Phan tu am dau tien trong list la: ", so_am[0])
print("Phan tu lon nhat la: ", lon_nhat, "va co index la: ", a.index(lon_nhat))