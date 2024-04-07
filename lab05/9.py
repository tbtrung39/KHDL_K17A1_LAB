str1 = str(input("nhập chuỗi 1: "))
str2 = str(input("Nhập chuỗi 2: "))
a = ''.join(i for i in str1 if i in str2)
print(a)