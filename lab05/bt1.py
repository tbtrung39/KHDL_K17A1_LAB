a = input("Nhập chuỗi kí tự: ")
dem = 0
for c in a: 
    if "0" <= c <= "9": 
        dem += 1 
print("Số các ký tự là số trong chuỗi đã nhập: ",dem) 