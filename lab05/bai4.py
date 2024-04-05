str1 = input("nhập vào chuỗi thứ nhất: ")
str2 = input("nhập vào chuỗi thứ hai: ")
result = ''
len1 = len(str1)
len2 = len(str2)
t1 = 0
t2 = 0
while t1 < len1 and t2 < len2:
    result += str1[t1] + str2[t2]
    t1 += 1
    t2 += 1
if t1 < len1:
    result += str1[t1:]
if t2 < len2:
    result += str2[t2:]
print("kết quả sau khi trộn:", result)