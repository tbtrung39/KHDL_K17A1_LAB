#6.1
import random
A = [random.randint(1, 99999) for _ in range(1000)]
sorted_A = sorted(A)
print("Danh sách A đã sắp xếp bằng hàm sorted():")
print(sorted_A)
#6.2
import random
A = [random.randint(1, 99999) for _ in range(1000)]
for i in range(len(A)):
    for j in range(len(A) - 1 - i):
        if A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]
print("Danh sách A đã sắp xếp không sử dụng hàm sorted():")
print(A)