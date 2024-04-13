n=int(input("Nhập số phần tử trong ds:"))
ds=[]
for i in range(n):
    phan_tu=int(input("nhập phần tử vào ô trống:"))
    ds.append(phan_tu)
print("Danh sách các phần tử:",ds)
ds_sap_xep=sorted(ds,reverse=True)
phan_tu_lon_thu_hai=ds_sap_xep[1]
print("Phần tử lớn thứ hai:",phan_tu_lon_thu_hai)
print("Vị trí phần tử lớn thứ hai luôn là 1")