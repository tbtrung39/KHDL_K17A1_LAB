n = input("Nhập chuỗi kí tự: ")
dem = 0
for char in n:
    if not char.isalpha() and not char.isdecimal():
        dem += 1
print("Số kí tự không phải là chữ cái tiếng anh và không phải là số là:", dem)