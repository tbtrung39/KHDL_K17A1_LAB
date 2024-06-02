'''
Cho trước (hoặc nhập vào từ bàn phím) chuỗi ký tự Str. 
Hãy xóa đi tất cả các ký tự Str không phải là số, chuỗi ký tự còn lại sẽ là số. 
In ra kết quả chuỗi số này và thông báo cho biết chuỗi đó có phải là số hoàn hảo không.
'''
str1 = input("Nhập một chuỗi từ bàn phím: ")
str2 = ""
for i in str1:
    if i.isnumeric():
        str2 += i
print("Chuỗi chỉ gồm số sau khi tách từ chuỗi ban đầu là:", str2)
#Chuyển kiểu dữ liệu từ chuỗi sang số
so_str2 = int(str2)
sum = 0
for i in range(1,so_str2):
    if so_str2 % i == 0:
        sum += i 
if sum == so_str2:
    print("Chuỗi số đã tách là số hoàn hảo")