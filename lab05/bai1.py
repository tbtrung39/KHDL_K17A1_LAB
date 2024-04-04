n = str(input("nhập vào một chuỗi ký tự: "))
dem = 0 
for char in n:
    if char.isdigit():
        dem +=1
print(f"số ký tự trong chuỗi là {dem}")