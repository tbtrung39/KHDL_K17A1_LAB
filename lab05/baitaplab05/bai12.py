A = input("Nhập chuỗi ký tự A: ")
B = input("Nhập chuỗi ký tự B: ")
found_solution = False
for i in range(1, len(A)):
    for j in range(1, len(B)):
        C, D = A[:i], A[i:]
        E, F = B[:j], B[j:]
        if int(C) + int(D) == int(E) + int(F):
            print(f"{C}+{D}={E}+{F}")
            found_solution = True
            break
    if found_solution:
        break
#if not found_solution:
 #   print("Không tồn tại cách đặt!")