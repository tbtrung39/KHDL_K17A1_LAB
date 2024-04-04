Str = input("Nhập chuỗi ký tự: ")
sum = 0
for i in Str:
    if '0' <= i <= '9':
        sum += 1
print("Số ký tự là số từ 0 đến 9 trong chuỗi là:", sum)
