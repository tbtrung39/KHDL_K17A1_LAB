tap_hop_A = {1, 2.5, "Hello", 3, 4.6, "World", 5, "Python", 6.2}
so_nguyen = sum(isinstance(x, int) for x in tap_hop_A)
so_thuc = sum(isinstance(x, float) for x in tap_hop_A)
so_chuoi = sum(isinstance(x, str) for x in tap_hop_A)
print("Số phần tử là số nguyên trong tập hợp A:", so_nguyen)
print("Số phần tử là số thực trong tập hợp A:", so_thuc)
print("Số phần tử là chuỗi ký tự trong tập hợp A:", so_chuoi)