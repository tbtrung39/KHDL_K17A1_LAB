import random

A = set(input("Nhập các phần tử của tập hợp A, cách nhau bằng dấu cách: ").split())

B = set(input("Nhập các phần tử của tập hợp B, cách nhau bằng dấu cách: ").split())

phan_tu_chung = A.intersection(B)
print("Các phần tử chung của tập hợp A và tập hợp B là:", phan_tu_chung)

