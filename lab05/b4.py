str1 = input("Nhập chuỗi ký tự thứ nhất (Str1): ")
str2 = input("Nhập chuỗi ký tự thứ hai (Str2): ")

mixed_string = ""

len_str1 = len(str1)
len_str2 = len(str2)

max_length = max(len_str1, len_str2)

for i in range(max_length):
    if i < len_str1:
        mixed_string += str1[i]
    if i < len_str2:
        mixed_string += str2[i]

print("Chuỗi kết quả sau khi trộn là:", mixed_string)
