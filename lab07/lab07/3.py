import random
n = int(input("Nhập vào số lượng phần tử của tập hợp A: "))
A = [random.uniform(-10, 10) for _ in range(n)]
min_element = min(A)
max_element = max(A)
sum_elements = sum(A)
print("Tập hợp A:", A)
print("Phần tử nhỏ nhất:", min_element)
print("Phần tử lớn nhất:", max_element)
print("Tổng các phần tử:", sum_elements)
