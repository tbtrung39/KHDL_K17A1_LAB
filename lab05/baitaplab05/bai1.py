str = input("Nhập vào chuỗi:")
dem = 0
for c in str:
    if c.isnumeric():
        dem+=1
print("Keys is numbers:",dem)