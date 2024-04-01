A = input("nhập chuỗi ký tự A: ")
B = input("nhập chuỗi ký tự B: ")
len_A = len(A)
len_B = len(B)
k = ""
for i in range(1, len_A):
    for j in range(1, len_B):
        C = A[:i]
        D = A[i:]
        E = B[:j]
        F = B[j:]
        if int(C) + int(D) == int(E) + int(F):
            k = f"{C}+{D}={E}+{F}"
            break
if k:
    print(k)
else:
    print("không tồn tại ")
