import random

A = [random.randint(1, 99999) for _ in range(1000)]
'''print(A)
A_sorted = sorted(A)
print(A_sorted)'''
A_sorted = A.copy()
A_sorted.sort()
print(A_sorted)