
# Nhập dữ liệu từ bàn phím và tạo tập hợp A
A = set(input("Nhập các ký tự chữ và số cho tập hợp A, cách nhau bằng dấu cách: ").split())

# Nhập dữ liệu từ bàn phím và tạo tập hợp B
B = set(input("Nhập các ký tự chữ và số cho tập hợp B, cách nhau bằng dấu cách: ").split())

# Liệt kê các phần tử chung của hai tập hợp A và B
phần_tử_chung = A.intersection(B)
print("Các phần tử chung của hai tập hợp A và B:", phần_tử_chung)