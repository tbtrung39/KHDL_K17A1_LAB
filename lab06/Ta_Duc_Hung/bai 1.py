# câu 1
a=[2,-4,1,9,-3,6,3,-2,6,8]
# tính tỏng các phần tử của danh sách 
tong=sum(a)
print("tổng của list a là :",tong)
# đếm số lượng 
so_luong_phan_tu_duong=0
for i in a :
    if i >0:
        so_luong_phan_tu_duong +=1

b=[]
for j in a:
    if j >0:
        b.append(j)
        tong_pt_duong=sum(b)
print("só lượng phần tử dương là :",so_luong_phan_tu_duong)
print("tổng các phần tử dương là :",tong_pt_duong)
vi_tri_am_dau_tien=None
for k in range(len(a)):
    if a[k] <0:
        vi_tri_am_dau_tien = k
        break
if vi_tri_am_dau_tien != None:
    print("Vị trí âm đầu tiên trong danh sách là ",vi_tri_am_dau_tien)
else:
    print("không có phần tử âm ")
vi_tri_duong_cuoi_cung=None
for i in range(len(a) -1, -1, -1):
    if a[i]>0:
        vi_tri_duong_cuoi_cung=1
        break
if vi_tri_duong_cuoi_cung != None:
    print("Vị trí đường cuối cùng là :",vi_tri_duong_cuoi_cung)
else:
    print("Không có vị trí đường cuối cùng trong danh sách ")
phan_tu_max=max(a)
vi_tri=a.index(phan_tu_max)
print("phần tử lớn nhất là :",phan_tu_max)
print("vị trí phần tử max là :" ,vi_tri)
