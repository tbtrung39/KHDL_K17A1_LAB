str = input("Nhập chuỗi ký tự: ")
count = 0
for char in str:
    if not char.isalpha() and not char.isdecimal():
        count += 1
    print(count)