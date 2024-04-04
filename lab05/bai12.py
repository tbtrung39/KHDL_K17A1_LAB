A = input("Nhập chuỗi ký tự A: ")
B = input("Nhập chuỗi ký tự B: ")
for i in range(1, len(A)):
    for j in range(1, len(B)):
        C = int(A[:i])
        D = int(A[i:])
        E = int(B[:j])
        F = int(B[j:])
        if C + D == E + F:
            print(f"{C}+{D}={E}+{F}")
            break
    else:
        continue
    break
else:
    print("Không tồn tại cách thêm dấu +")
