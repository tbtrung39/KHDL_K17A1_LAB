'''4. Cho trước 2 chuỗi ký tự Str1, Str2 (có thể nhập từ bàn phím). Viết chương trình trộn 
chuỗi /xâu ký tự 1 và 2. 
Việc trộn St1 và Str2 thực hiện theo nguyên tắc sau: 
- Lần lượt từ trái sang phải, viết các ký tự của Str1, sau đó đến Srt2. 
- Nếu một trong hai chuỗi kết thúc thì chỉ viết ra các ký tự của chuỗi còn lại'''
str1 = input("Nhập chuỗi ký tự thứ nhất: ")
str2 = input("Nhập chuỗi ký tự thứ hai: ")
merged_string = ''
min_len = min(len(str1), len(str2))
for i in range(min_len):
    merged_string += str1[i] + str2[i]
merged_string += str1[min_len:] + str2[min_len:]
print("Chuỗi sau khi trộn:", merged_string)
