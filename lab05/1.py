n = input("nhập chuỗi kí tự: ")
s = 0
for char in n:
    if "0" <= char <= "9":
        s+=1
print("số kí tự đã nhập là: ", s)