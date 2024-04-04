# Nhập chuỗi ký tự nhị phân từ người dùng
a = input("Nhập chuỗi ký tự nhị phân: ")

# Chuyển đổi chuỗi nhị phân sang số thập phân
b = 0
for i in range(len(a)):
    b = b * 2 + int(a[i])

print(f"Số thập phân tương ứng với chuỗi nhị phân {a}")