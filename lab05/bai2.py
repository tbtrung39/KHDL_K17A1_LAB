Str = input("Nhập chuỗi ký tự: ")
tong = 0
for char in Str:  
    if not (char.isalpha() and char.isascii()) and not char.isdigit():
        tong += 1
print("số lượng các ký tự không phải chữ cái tiếng anh và không là số trong chuỗi là : ", tong)