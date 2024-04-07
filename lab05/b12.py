A = input("Nhập chuỗi ký tự A: ")
B = input("Nhập chuỗi ký tự B: ")

found = False
for i in range(1, len(A)):
    for j in range(1, len(B)):
        num1 = int(A[:i])
        num2 = int(A[i:])
        num3 = int(B[:j])
        num4 = int(B[j:])
        if num1 + num2 == num3 + num4:
            print(f"{num1}+{num2}={num3}+{num4}")
            found = True
            break
    if found:
        break

if not found:
    print("Không tồn tại cách đặt!")