import random as r
n=int(input('nhập n:'))
A=r.choices(range(0,n*n),k=n)
print(f'phần tử nhỏ nhất:{min(A)}\nphần tử lớn nhất:{max(A)}\ntổng các phần tử của A:{sum(A)}')