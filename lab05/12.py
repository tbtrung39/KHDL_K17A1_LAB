'''Cho chuỗi ký tự Str1. Ta gọi một từ trong chuỗi là một dãy ký tự liên tiếp (không có 
ký tự trắng và dấu phẩy) các từ này được phân cách bởi các ký tự trắng hoặc dấu phẩy.  
Ví  dụ: Str1 = “Khoa, khoa hoc ung dung” gồm  các  từ: “Khoa”, “khoa”, “học”, “ứng”, 
“dụng”. 
Hãy viết chương trình in ra các từ trong chuỗi Str1, mỗi từ in trên một dòng. 
'''
str = "khoa,khoa hoc ung dung"
a = str.split(" ")
if len(a)==1:
    a = str.split(",")
for word in a:
    print(a)