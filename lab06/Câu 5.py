'''
Viết chương trình sinh một dãy list A gồm 1000 số tự nhiên,
nằm ngẫu nhiên trong khoảng [1,99999].
'''
import random
A = []
for a in range(1000):
    so = random.randint(0,100000)
    A.append(so)
print("Danh sách A gồm 1000 số tự nhiên:")
print(A)