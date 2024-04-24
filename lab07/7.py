import random
a = set(input("Nhập tập hợp a (các phần tử cách nhau bằng khoảng trắng): ").split())
b = set(input("Nhập tập hợp b (các phần tử cách nhau bằng khoảng trắng): ").split())
print("Tập hợp a:", a)
print("Tập hợp b:", b)
c = a.intersection(b)
print("Các phần tử chung của tập hợp a và b:", c)