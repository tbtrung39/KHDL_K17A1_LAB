n = str(input("nhập vào một chuỗi ký tự: "))
dem = 0 
for char in n:
    if not (char.isalnum() or char.isdigit()):
        dem += 1
print(f"số lượng ký tự trong chuỗi ko phải tiếng anh hay số là {dem}")