import random

# Nhập các phần tử của tập hợp A từ bàn phím
tap_hop_A = set(input("Nhập các ký tự chữ và số cho tập hợp A (các phần tử cách nhau bằng khoảng trắng): ").split())

# Nhập các phần tử của tập hợp B từ bàn phím
tap_hop_B = set(input("Nhập các ký tự chữ và số cho tập hợp B (các phần tử cách nhau bằng khoảng trắng): ").split())

# Tìm và in ra các phần tử chung của A và B
phan_tu_chung = tap_hop_A.intersection(tap_hop_B)
print("Các phần tử chung của tập hợp A và B là:", phan_tu_chung)
