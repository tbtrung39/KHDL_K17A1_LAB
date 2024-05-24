'''
Cho trước (hoặc nhập vào từ bàn phím) chuỗi ký tự Str, 
có bao nhiêu ký tự không phải là chữ cái tiếng Anh và không là số trong chuỗi ký tự Str.
'''
chuoi = input("Nhập vào một chuỗi: ")
count = 0 
for i in chuoi:
    if i.isnumeric():
        count -= 1 
    else:
        for a in range(65,91):
            if i == chr(a):
                count -= 1 
        for b in range(97, 123):
            if i == chr(b):
                count -= 1
    count += 1
print("Số ký tự không phải chữ cái tiếng Anh và số là:", count)