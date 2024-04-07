'''1. Nhập từ bàn phím một chuỗi ký tự Str. Hãy đếm sô các ký tự là số trong chuỗi ký tự Str 
và in kết quả ra màn hình'''
string = input("Nhập chuỗi ký tự: ")
count = 0
for char in string:
    if char.isdigit():
        count += 1
print("Số ký tự là số trong chuỗi:", count)