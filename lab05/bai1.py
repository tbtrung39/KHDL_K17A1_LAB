
Str = input("Nhập chuỗi ký tự: ")
tong = 0
for char in Str:
    if char.isdigit():
        tong += 1
print("Số lượng các ký tự là số trong chuỗi là:", tong)
