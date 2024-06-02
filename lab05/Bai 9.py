'''
Cho trước hoặc nhập từ bàn phím 2 chuỗi ký tự Str1 và Str2. 
Hãy viết chương trình tìm ra chuỗi ký tự con chung của 2 chuỗi ký tự Str1, Str2 
có độ dài cực đại.
Str1 = "abcdef"
Str2 = "aabbc"
Output:
chuoi = "aabbc"
'''
str1 = input("Nhập vào chuỗi thứ nhất: ")
str2 = input("Nhập vào chuỗi thứ hai: ")
max_chuoi = ""
chuoi_con = ""
for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i] == str2[j]:
            #Xây dựng chuỗi con
            k = 0
            while (i + k) < len(str1) and (j + k) < len(str2) and str1[i+k] == str2[j + k]:
                chuoi_con += str1[i + k]
                k += 1 
            #Kiểm tra độ dài chuỗi con
            if len(chuoi_con) > len(max_chuoi):
                max_chuoi = chuoi_con
            #Reset chuỗi con
            chuoi_con = ""
print("Chuỗi ký tự con chung của 2 chuỗi đã cho và có độ dài cực đại là:", max_chuoi)