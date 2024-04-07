'''2. Cho trước (hoặc nhập từ bàn phím) chuỗi ký tự Str, có bao nhiêu ký tự không phải là 
chữ cái tiếng Anh và không là số trong chuỗi Str'''
string = input("Nhập chuỗi ký tự: ")
count = 0
for char in string:
    if not char.isalpha() and not char.isdigit():
        count += 1
print("Số ký tự không phải là chữ cái tiếng Anh hoặc số trong chuỗi:", count)
