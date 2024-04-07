str1 = str(input("Nhập chuỗi kí tự 1: "))
str2 = str(input("Nhập chuỗi kí tự 2: "))
a = ''.join(i for i in str1 if i in str2)
print(f"Kí tự con chung của 2 chuỗi là: ",a)



