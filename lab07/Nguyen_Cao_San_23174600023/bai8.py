A = {1, 2.5, "hello", 3, 4.8, "world", 5, 6, "python"}

# Đếm số phần tử là số nguyên, số thực và chuỗi ký tự của tập hợp A
so_luong_so_nguyen = sum(isinstance(x, int) for x in A)
so_luong_so_thuc = sum(isinstance(x, float) for x in A)
so_luong_chuoi = sum(isinstance(x, str) for x in A)

# In kết quả
print("Số phần tử là số nguyên trong tập hợp A:", so_luong_so_nguyen)
print("Số phần tử là số thực trong tập hợp A:", so_luong_so_thuc)
print("Số phần tử là chuỗi ký tự trong tập hợp A:", so_luong_chuoi)
