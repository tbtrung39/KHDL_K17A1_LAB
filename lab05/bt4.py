m = input("Nhập chuỗi kí tự Str1: ")
n = input("Nhập chuỗi kí tự Str2: ")
i = 0; j = 0
a = ""
while i < len(m) and j < len(n):
    a += m[i] + n[j]
    i += 1
    j += 1
print("Chuỗi lần lượt kí tự Str1-Str2 là: ",a)
b = ''
while i < len(m):
    b += m[i]
    i += 1
while j < len(n):
    b += n[j]
    j += 1
print("Kí tự chuỗi còn lại là: ",b)
