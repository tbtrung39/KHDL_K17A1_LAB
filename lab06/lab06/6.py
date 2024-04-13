import random
A = [random.randint(1, 99999) for _ in range(1000)]
A_sorted = sorted(A)
for i in range(len(A)):
    for j in range(i + 1, len(A)):
        if A[i] > A[j]:
            A[i], A[j] = A[j], A[i]
print("Danh sách A sau khi sắp xếp bằng hàm sorted():",A_sorted)
print("Danh sách A sau khi sắp xếp mà không sử dụng hàm sorted():",A)
