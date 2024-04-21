import random
n = int(input("Nhập số lượng phần tử của tập hợp: "))
A = set(random.uniform(0, 100) for _ in range(n))
min_A = min(A)
max_A = max(A)
sum_A = sum(A)
print("Tập hợp A:", A)
print("Phần tử nhỏ nhất trong tập hợp A:", min_A)
print("Phần tử lớn nhất trong tập hợp A:", max_A)
print("Tổng của tập hợp A:", sum_A)











'''import math
n=int(input('Nhập số lượng phần tử của A :'))
setA.add(num)
phan_tu_nho_nhat=min(setA)
phan_tu_lon_nhat=max(setA)
tong_phan_tu=sum(setA)
print('Tập hợp A là :',setA)
print('Phần tử nhỏ nhất là :',phan_tu_nho_nhat)
print('Phần tử lớn nhất là :',phan_tu_lon_nhat)
print('Tổng các phần tử là :',tong_phan_tu)'''