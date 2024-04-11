import random

# Nhập số lượng phần tử của tập hợp từ người dùng
so_luong_phan_tu = int(input("Nhập số lượng phần tử của tập hợp A: "))

# Sinh ngẫu nhiên tập hợp A gồm n số thực
tap_hop_A = set(random.uniform(0, 100) for _ in range(so_luong_phan_tu))

# Tìm phần tử nhỏ nhất, lớn nhất và tổng các phần tử của tập hợp A
phan_tu_nho_nhat = min(tap_hop_A)
phan_tu_lon_nhat = max(tap_hop_A)
tong_cac_phan_tu = sum(tap_hop_A)

# In ra kết quả
print("Tập hợp A:", tap_hop_A)
print("Phần tử nhỏ nhất trong tập hợp A:", phan_tu_nho_nhat)
print("Phần tử lớn nhất trong tập hợp A:", phan_tu_lon_nhat)
print("Tổng các phần tử trong tập hợp A:", tong_cac_phan_tu)
