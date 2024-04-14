a=[2,-4,1,9,.4,6,3,-2,6,8]
S=sum(a)
so_duong=sum([i for i in a if i >=0])
so_am =[i for i in a if i <0]
phan_tu_duong_cuoi = [i for i in a if i>=0]
lon_nhat= max(a)
print("tong cac phan tu la:",S)
print("tong cac so duong la:",so_duong)
print("phan tu am dau tien trong list la:",so_am[0])
print("phan tu am ccuoi cung trong list la:",phan_tu_duong_cuoi[-1])
print("phan tu am lon nhat la:",lon_nhat,"va co in dex la:",a.index(lon_nhat))
