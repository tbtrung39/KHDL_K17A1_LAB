'''
Cho danh sách a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8] gồm n = 10 phần tử.
Yêu cầu:
- Viết chương trình Python tính tổng các phần tử của danh sách.
- Viết chương trình Python đếm số lượng các số hạng dương và tổng của các số hạng dương.
- Tìm vị trí của phần tử âm đầu tiên trong danh sách.
- Tìm vị trí của phần tử dường cuối cùng trong danh sách.
- Tìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất cuối cùng.
'''
#Nhập danh sách
a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]

#Tính tổng các phần tử của danh sách
tong_phan_tu = sum(a)
print("Tổng các phần tử là: ", tong_phan_tu)

#Đếm số lượng các số hạng dương và tổng của các số hạng dương
so_luong_so_duong = 0
tong_so_duong = 0
for num in a:
    if num > 0:
        so_luong_so_duong += 1
        tong_so_duong += num
print("Số lượng số dương:", so_luong_so_duong)
print("Tổng các số dương:", tong_so_duong)

#Tìm vị trí của phần tử âm đầu tiên trong danh sách
vi_tri_ptu_am_dau = next((i for i, x in enumerate(a) if x < 0), None)
print("vị trí của phần tử âm đầu tiên là: ", vi_tri_ptu_am_dau)


#Tìm vị trí của phần tử dương cuối cùng trong danh sách
vi_tri_ptu_duong_cuoi = len(a) - a[::-1].index(next((x for x in a[::-1] if x > 0), None)) - 1
print("vị trí của phần tử dương cuối cùng là: ", vi_tri_ptu_duong_cuoi)


#Tìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất cuối cùng
ptu_lon_nhat = max(a)
vi_tri_ptu_cuoi_lon_nhat = len(a) - a[::-1].index(ptu_lon_nhat) - 1
print("Phần tử lớn nhất của danh sách:", ptu_lon_nhat)
print("Vị trí phần tử lớn nhất cuối cùng trong danh sách:", vi_tri_ptu_cuoi_lon_nhat)