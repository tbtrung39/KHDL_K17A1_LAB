# Nhập giá trị X và Y từ người dùng
X = int(input("Nhập giá trị X: "))
Y = int(input("Nhập giá trị Y: "))

# Tạo mảng 2 chiều theo yêu cầu
z = [[i*j for j in range(Y)] for i in range(X)]

# In ra mảng 2 chiều đã tạo
for row in z:
    print(row)
