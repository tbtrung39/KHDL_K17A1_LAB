import random
A = set(input("Nhập các phần tử cho tập hợp A (các ký tự chữ và số, phân tách bằng dấu cách): ").split())
B = set(input("Nhập các phần tử cho tập hợp B (các ký tự chữ và số, phân tách bằng dấu cách): ").split())
print("Các phần tử chung của A và B:")
common_elements = A.intersection(B)
for element in common_elements:
    print(element)