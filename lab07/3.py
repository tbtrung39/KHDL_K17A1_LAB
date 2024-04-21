import random
n = int(input("Nhập số lượng phần tử của tập hợp: "))
A = set(random.uniform(0, 100) for _ in range(n))

min_A = min(A)
max_A = max(A)
sum_A = sum(A)

# In kết quả
print("Tập hợp A:", A)
print("Phần tử nhỏ nhất trong tập hợp A:", min_A)
print("Phần tử lớn nhất trong tập hợp A:", max_A)
print("Tổng của tập hợp A:", sum_A)