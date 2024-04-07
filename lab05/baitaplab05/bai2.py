str = input("Nhập vào chuỗi str:")
dem = 0
for c in str:
    if not c.isnumeric() and not c.isalpha():
        dem+=1
print("numbers and alpha not in str:",dem)