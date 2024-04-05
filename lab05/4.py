str1 = input("Nhap chuoi s1: ")
str2 = input("Nhap chuoi s2: ")
a = ""
i = 0
while i < len(str1) or i < len(str2):
    if i < len(str1):
        a += str1[i]
    if i < len(str2):
        a += str2[i]
    i += 1
print("Chuoi sau khi duoc tron la: ", a)
if len(str1) != len(str2):
    if len(str1) > len(str2):
        print("Chuoi con lai: ", str1[len(str2):])
    else:
        print("Chuoi conlai: ", str2[len(str1):])
