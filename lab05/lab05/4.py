str1 = input("Nhập chuỗi ký tự 1: ")
str2 = input("Nhập chuỗi ký tự 2: ")
len_str1 = len(str1)
len_str2 = len(str2)
i = 0
j = 0
xao_tron = ""
while i < len_str1 and j < len_str2:
    xao_tron += str1[i] + str2[j]
    i += 1
    j += 1
xao_tron += str1[i:]
xao_tron += str2[j:]
print("Chuỗi kết quả sau khi trộn là:", xao_tron)
