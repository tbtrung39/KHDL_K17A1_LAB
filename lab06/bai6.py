import random
A = [random.randint(1, 99999) for i in range(1000)]
print(A)
#sắp xếp theo thứ tự tăng dần
A.sort()
print(f"A sau khi sắp xếp theo thứ tự tăng dần là:{A}")
#sắp xếp tăng dần ko dùng sort()
for i in range(len(A)):
    nho_nhat = i
    for j in range(i+1, len(A)):
        if A[j] < A[nho_nhat]:
            nho_nhat = j
    A[i], A[nho_nhat] = A[nho_nhat], A[i]
print(f"Danh sách A sau khi sắp xếp tăng dần là: {A}")