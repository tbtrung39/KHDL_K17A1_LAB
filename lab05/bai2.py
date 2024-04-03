n = input("Nhập chuỗi: ")
s = 0
q = 0
for char in n:
    if "0" <= char <= "9":
        s+=1
    if char.isalpha():
        q+=1

print("số kí tự ko là tiếng anh là: ", s)
print("số ki kí tự ko phải là số là: ", q)