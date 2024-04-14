# Nhập giá trị của X và Y từ người dùng
X = int(input("Nhập giá trị của X: "))
Y = int(input("Nhập giá trị của Y: "))

# Tạo mảng 2 chiều theo yêu cầu
mang_2_chieu = [[i * j for j in range(Y)] for i in range(X)]

# In mảng ra màn hình
for hang in mang_2_chieu:
    print(hang)