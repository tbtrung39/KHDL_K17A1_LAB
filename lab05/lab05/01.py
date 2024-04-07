Str = input("Nhập chuỗi ký tự: ")
count = 0 #count là biến đếm
#đếm số lượng
for char in Str:
    if char.isdigit():
        count += 1
print(count)