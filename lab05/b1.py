n = input("Nhập chuỗi kí tự: ")
dem = 0
for char in n:
    if char.isdigit():
        dem += 1
print("Số các ký tự là số trong chuỗi đã nhập =",dem)