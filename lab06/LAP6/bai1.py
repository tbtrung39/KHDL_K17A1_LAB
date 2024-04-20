a = [2,-4,1,9,-3,6,3,-2,6,8]
tong_cac_ptu=sum(a)
print('Tong cac phan tu la: ',tong_cac_ptu)

# phan tu duong
phan_tu_duong=[]
for i in a:
    if i >0:
        phan_tu_duong.append(i)
print(phan_tu_duong)
print('Tổng các phần tử dương là: ',sum(phan_tu_duong))

# tim phan tu am dau tien
phan_tu_am = ''
for n in a:
    if n<0:
        phan_tu_am = n
        break
print("Phan tu am dau tien la:",phan_tu_am)

# tim vi tri phan tu duong cuoi cung trong danh sach
pt_duong = ''
for m in a:
    if m>0:
        pt_duong = m
print('Phan tu duong cuoi cung trong list la:',pt_duong)

# tim phan tu lon nhat
phan_tu_lon_nhat = max(a)
print('Phan tu lon nhat trong list la:', phan_tu_lon_nhat)
