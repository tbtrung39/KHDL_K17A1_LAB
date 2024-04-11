import random

# Danh sách chứa các chữ số từ 0 đến 9
danh_sach = list(range(10))

# Tạo tập hợp A gồm 5 phần tử ngẫu nhiên từ danh sách trên
A = set(random.sample(danh_sach, 5))

# In ra tập hợp A
print("Tập hợp A:", A)
