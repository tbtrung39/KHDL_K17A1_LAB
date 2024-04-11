a = [2,-4,1,9,-3,6,3,-2,6,8] 
tong = sum(a)
print("tổng của list trong danh sách là:",tong)
so_phan_tu_duong = 0
for i in a:
    if i > 0:
        so_phan_tu_duong += 1
b = []
for j in a :
    if j > 0 :
        b.append(j)
        tong_pt_duong = sum(b)
print("số phần tử dương ",so_phan_tu_duong)
print("tổng các phân tử dương là:",tong_pt_duong)
vi_tri_dau = None
for k in range(len(a)):
    if a[k] <0:
        vi_tri_dau = k
        break
if vi_tri_dau != None:
    print("vị trí đầu tiên trong danh sách là:", vi_tri_dau)
else:
    print("không có phần tử trong danh sách ")
so_duong_cuoi_cung = None
for i in range(len(a) - 1,-1,-1):
    if a[i] > 0:
        so_duong_cuoi_cung = i
        break
if so_duong_cuoi_cung != 0:
    print("số dương cuối cùng là",so_duong_cuoi_cung)
else:
    print("không có phần tử nào trong danh sách")
phan_tu_lon_nhat = max(a)
vi_tri = a.index(phan_tu_lon_nhat)
print("phần tử lớn nhất là:", phan_tu_lon_nhat)
print("vị trí phần tử lớn nhất là:", vi_tri)
