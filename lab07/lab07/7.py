import random
a = set(input("Nhập vào các phần tử của tập hợp A: ").split())
b = set(input("Nhập vào các phần tử của tập hợp B: ").split())
intersection = a.intersection(b)
print(f"Các phần tử của A và B: {intersection}")
