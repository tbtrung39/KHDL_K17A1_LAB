import math
n = input("Nhập chuỗi ký tự: ")
a = ""
for char in n:
    if char.isdigit():
        a += char
print("Chuỗi số sau khi xóa các ký tự không phải là số:", a)
sum_num = int(a)
b = sum(i for i in range(1, sum_num) if sum_num % i == 0)
c = b == sum_num

if c:
    print("Chuỗi số là số hoàn hảo.")
else:
    print("Chuỗi số không phải là số hoàn hảo.")
