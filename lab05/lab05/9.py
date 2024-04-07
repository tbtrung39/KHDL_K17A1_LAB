str1 = str(input("nhap chuoi 1: "))
str2 = str(input("Nhap chuoi 2: "))
a = ''.join(i for i in str1 if i in str2)
print(a)