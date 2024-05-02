import random
so_luong_phan_tu = int(input("Nhập số lượng phần tử của tập hợp A: "))
tap_hop_A = {random.uniform(0, 100) for i in range(so_luong_phan_tu)}
phan_tu_nho_nhat = min(tap_hop_A)
phan_tu_lon_nhat = max(tap_hop_A)
tong_phan_tu = sum(tap_hop_A)
print("Tập hợp A:", tap_hop_A)
print("Phần tử nhỏ nhất trong tập hợp A:", phan_tu_nho_nhat)
print("Phần tử lớn nhất trong tập hợp A:", phan_tu_lon_nhat)
print("Tổng các phần tử trong tập hợp A:", tong_phan_tu)
