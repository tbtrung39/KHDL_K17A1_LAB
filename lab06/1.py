a = [2,-4,1,9,-3,6,3,-2,6,8]
print("tong la", sum(a))

so_luong_duong=0
tong_so_duong=0
for i in a :
    if i >0:
        so_luong_duong+=1
        tong_so_duong+=i
print("so luong so duong trong a la",so_luong_duong)
print('tong so duong trong a la',tong_so_duong)
# tim vị trí của phần tử aam trong danh sách 
vi_tri_am_dau_tien=a.index(-4)
print(" vị trí âm đầu tiên là ",vi_tri_am_dau_tien)
vi_tri_duong_cuoi_cung=a.index(8)
print(" vị trí dương cuối cùng là ", vi_tri_duong_cuoi_cung)
# tìm phần tử lớn nhất của danh sách , và tìm vị trí 
print(" phần tử lớnn nhất của danh sách là ",max(a))
vi_tri_ptu_lon_nhat=a.index(max(a))
print("vị trí phần tử lớn nhất là ",vi_tri_ptu_lon_nhat)



