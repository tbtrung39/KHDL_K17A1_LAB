'''
Cho trước 2 chuỗi ký tự Str1, Str2 (nhập vào từ bàn phím). 
Viết chương trình trộn chuỗi ký tự 1 và 2. Việc trộn Str1 và Str2 thực hiện theo quy tắc sau:
+ Lần lượt từ trái sang phải, viết các ký tự của Str1, sau đó đến Str2
+ Nếu một trong hai chuỗi kết thúc thì chỉ viết ra các ký tự của chuỗi còn lại
Input:
Str1 = “abc”
Str2 = “ghi”
Output: “agbhci”
'''

str1 = input("Nhập vào chuỗi thứ nhất: ")
str2 = input("Nhập vào chuỗi thứ hai: ")
chuoi_gop = ""
min_length = 0
if len(str1) < len(str2):
    min_length = len(str1)
else:
    min_length = len(str2)
for i in range(min_length):
    chuoi_gop += str1[i] + str2[i]

#Xử lý phần còn lại của chuỗi dài hơn
if len(str1) < len(str2):
    chuoi_gop += str2[min_length:]
else:
    chuoi_gop += str1[min_length:]

print("Chuỗi trộn của hai chuỗi đã nhập là:", chuoi_gop)