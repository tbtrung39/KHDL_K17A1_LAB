# Nhập chuỗi A và B từ người dùng
A = input("Nhập chuỗi A: ")
B = input("Nhập chuỗi B: ")

n = len(A)
m = len(B)
found = False

# Duyệt qua các vị trí trong chuỗi A để chèn dấu "+" vào giữa các chữ số
for i in range(1, n):
    for j in range(1, m):
        C = int(A[:i])
        DE = int(A[i:])
        F = int(B[:j])
        G = int(B[j:])
        if C + DE == F + G:
            result = A[:i] + "+" + A[i:] + "=" + B[:j] + "+" + B[j:]
            print(result)
            found = True
            break
    if found:
        break

if not found:
    print("Không tồn tại cách đặt")