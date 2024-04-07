str1 = input("Nhập chuỗi ký tự 1: ")
str2 = input("Nhập chuỗi ký tự 2: ")
len1 = len(str1)
len2 = len(str2)
ket_qua = ''
#trộn chuỗi
index1 = 0
index2 = 0
while index1 < len1 or index2 < len2:
    if index1 < len1:
        ket_qua = str1[index1]
        index1 += 1
    if index2 < len2:
        ket_qua = str2[index2]
        index2 += 1
print(f"chuỗi sau khi trộn là {ket_qua}")