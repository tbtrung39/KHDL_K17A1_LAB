a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
# Tính tổng các phần tử của danh sách
print('Tổng các phần tử của danh sách là:', sum(a))
# Đếm số lượng số hạng dương và tính tổng các số hạng dương
so_hang_duong = [x for x in a if x > 0]
so_luong_so_hang_duong = len(so_hang_duong)
tong_so_hang_duong = sum(so_hang_duong)
print('Các số hạng dương trong danh sách là:', so_hang_duong)
print('Số lượng số hạng dương trong danh sách là:', so_luong_so_hang_duong)
print('Tổng các số hạng dương trong danh sách là:', tong_so_hang_duong)
#Tìm vị trí phần tử âm đầu tiên trong danh sách
tim_thay_am = False
vi_tri_am_dau_tien = -1  
for i in range(len(a)):
    if a[i] < 0:
        tim_thay_am = True
        vi_tri_am_dau_tien = i
        break
if tim_thay_am:
    print('Vị trí của phần tử âm đầu tiên trong danh sách là:', vi_tri_am_dau_tien)
else:
    print('Không có phần tử âm trong danh sách.')
#vị trí phần tử dương cuối cùng
tim_thay_duong = False
vi_tri_duong_cuoi_cung = -1 
for i in range(len(a)):
    if a[i] > 0:
        tim_thay_duong = True
        vi_tri_duong_cuoi_cung = i
if tim_thay_duong:
    print('Vị trí của phần tử dương cuối cùng trong danh sách là:', vi_tri_duong_cuoi_cung)
else:
    print('Không có phần tử dương trong danh sách.')
#phần tử lớn nhất trong danh sách và vị trí
a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]

phần_tử_lớn_nhất = max(a)
vị_trí_phần_tử_lớn_nhất = a.index(phần_tử_lớn_nhất)
print('Phần tử lớn nhất trong danh sách là:', phần_tử_lớn_nhất)
print('Vị trí của phần tử lớn nhất trong danh sách là:', vị_trí_phần_tử_lớn_nhất)
