'''
Viết chương trình tạo tập hợp A gồm 5 phần từ ngẫu nhiên được lấy từ một 
danh sách 10 phần tử là các chữ số từ 0,1,...9.
'''
import random
danh_sach = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
A = set(random.sample(danh_sach, 5))

print("Tập hợp A:", A)