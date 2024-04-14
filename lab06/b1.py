a = [2, - 4, 1, 9, - 3, 6, 3, - 2, 6, 8]
sum_a = sum(a)
print("Tổng các phần tử trong danh sách là:", sum_a)
sl_duong = sum(1 for i in a if i > 0) 
tong_duong = sum(i for i in a if i > 0)

print("Số lượng các số hạng dương là:", sl_duong)
print("Tổng các số hạng dương là:", tong_duong)

vi_tri_am_dau_tien = a.index(next((x for x in a if x < 0 ), None))
print("Vị trí âm của phần tử đầu tiên trong danh sách là:", vi_tri_am_dau_tien)

vi_tri_duong_cuoi_cung = len(a) - a[::-1].index(next((x for x in a if x > 0), None)) - 1
print("Vị trí dương cuối cùng trong danh sách là:",vi_tri_duong_cuoi_cung)

phan_tu_lon_nhat = max(a)

vi_tri_lon_nhat_cuoi_cung = len(a) - a[::-1].index(phan_tu_lon_nhat) - 1

print("Phần tử lớn nhất trong danh sách là:", phan_tu_lon_nhat)
print("Vị trí phần tử lớn nhất cuối cùng trong danh sách là:", vi_tri_lon_nhat_cuoi_cung)