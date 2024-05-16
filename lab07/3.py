import random
n = 5  
a = {random.uniform(0, 100) for _ in range(n)}
min_element = min(a)
max_element = max(a)
sum_elements = sum(a)
print("Tập hợp a:", a)
print("Phần tử nhỏ nhất:", min_element)
print("Phần tử lớn nhất:", max_element)
print("Tổng các phần tử:", sum_elements)