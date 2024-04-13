A = []
B = []
C = []
D = []
while True:
    n = int(input("Nhập số nguyên (nhập 0 để kết thúc): "))
    if n == 0:
        break
    A.append(n)
print("Danh sách A vừa nhập vào là: ",A)
for i in A:
    C.append(i**2)
    if i % 3 == 0 and i % 5 != 0:
        B.append(i)
    if i % 3 ==0:
        D.append(i)
print("Các số trong danh sách A chia hết cho 3 nhưng không chia hết cho 5 là: ",B)
print("Danh sách C với các phần tử bình phương của danh sách A là: ",C)
print("Danh sách D gồm các phần tử lấy từ danh sách A chia hết cho 3 là: ",D)