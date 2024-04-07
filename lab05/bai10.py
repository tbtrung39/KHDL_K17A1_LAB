
Str1 = input("Nhập chuỗi ký tự thứ nhất: ")
Str2 = input("Nhập chuỗi ký tự thứ hai: ")
matrix = [[0] * (len(Str2) + 1) for _ in range(len(Str1) + 1)]
max_length = 0
end_index = 0
for i in range(1, len(Str1) + 1):
    for j in range(1, len(Str2) + 1):
        if Str1[i - 1] == Str2[j - 1]:
            if matrix[i][j] > max_length:
                max_length = matrix[i][j]
                end_index = i
common_substring = Str1[end_index - max_length: end_index]
print("Chuỗi ký tự con chung có độ dài cực đại là:", common_substring)
