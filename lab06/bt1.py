a = [2,-4,1,9,-3,6,3,-2,6,8]
#tinh tong
sum(a)
print(f"tong cua list a bang {sum(a)}")
#so hang duong va tong so hang duong
so_hang_duong = [x for x in a if x > 0]
so_luong_so_hang_duong=len(so_hang_duong)
tong_so_hang_duong= sum(so_hang_duong)
print(f"so luong hang duong bang {so_luong_so_hang_duong} va tong so luong hang duong bang {tong_so_hang_duong}")
# Tìm vị trí phần tử âm đầu tiên
for i in range(len(a)):
    if a[i] < 0:
        print("Vị trí của phần tử âm đầu tiên trong danh sách là:", i)
        break
# Tìm vị trí phần tử dương cuối cùng
chi_so_duong = False
for i in range(len(a)):
    if a[i] >0:
        chi_so_duong = i
if chi_so_duong is True:
    print(f"chi so duong cuoi cung la {chi_so_duong}")
else:
    print("khong co chi so duong cuoi cung")
## Tìm phần tử lớn nhất và vị trí của nó
gia_tri_max = max(a)
vi_tri_phan_tu_lon_nhat =a.index(gia_tri_max)
print(f"phan tu lon nhat la {gia_tri_max} va vi tri cua phan tu lon nhat la {vi_tri_phan_tu_lon_nhat}")
