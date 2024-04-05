str1 = input("Nhập chuỗi ký tự thứ nhất từ bàn phím: ")
str2 = input("Nhập chuỗi ký tự thứ hai từ bàn phím: ")

x1 = str1.split()
x2 = str2.split()
str3 = ''

for i in x1:
    if i in x2:
        str3 += i + ' '

print("Các từ chung trong hai chuỗi là:", str3.strip())
