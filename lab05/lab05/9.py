Str1 = input("Nhập chuỗi ký tự thứ nhất 1: ")
Str2 = input("Nhập chuỗi ký tự thứ hai 2: ")
len1 = len(Str1)
len2 = len(Str2)
dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
max_length = 0
end_index = 0
for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        if Str1[i - 1] == Str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            if dp[i][j] > max_length:
                max_length = dp[i][j]
                end_index = i
        else:
            dp[i][j] = 0
chuoi_con_chung = Str1[end_index - max_length: end_index]
print("Chuỗi ký tự con chung có độ dài cực đại là:", chuoi_con_chung)
