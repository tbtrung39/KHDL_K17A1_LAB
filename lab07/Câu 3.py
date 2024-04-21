'''
 Viết chương trình sinh một tập hợp A một cách ngẫu nhiên gồm n số thực (n được nhập từ bàn phím) 
 Tìm phần tử nhỏ nhất, lớn nhất và tổng các phần tử của tập hợp A.
'''
import random

n = int(input("Nhập số lượng phần tử của tập hợp: "))
random_numbers = [random.uniform(0, 100) for _ in range(n)]
A = set(random_numbers)

min_A = min(A)
max_A = max(A)
sum_A = sum(A)

print("Tập hợp A:", A)
print("Phần tử nhỏ nhất trong tập hợp A:", min_A)
print("Phần tử lớn nhất trong tập hợp A:", max_A)
print("Tổng của tập hợp A:", sum_A)
