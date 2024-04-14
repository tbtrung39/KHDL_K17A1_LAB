# Nhập giá trị X và Y từ người dùng
X = int(input("Nhập giá trị X: "))
Y = int(input("Nhập giá trị Y: "))

# Tạo mảng 2 chiều với giá trị phần tử là i*j
mang_2_chieu = [[i*j for j in range(Y)] for i in range(X)]

# In mảng 2 chiều
print("Mảng 2 chiều được tạo:")
for row in mang_2_chieu:
    print(row)
