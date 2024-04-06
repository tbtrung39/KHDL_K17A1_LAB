a = input("Nhập chuỗi kí tự: ")
dem = 0
for c in a:
    if not ('a'<=c<='z' or 'A'<=c<='Z' or '0'<=c<='9'):
        dem += 1
print("Số kí tự không là chữ cái TA và không là số: ",dem)