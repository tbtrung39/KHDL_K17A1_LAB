chuoi = input("nhập chuỗi của bạn:")
sum = 0 
for i in chuoi:
    if i.isalpha():
        sum += 1
    if "0" <= i <= "9":
        sum += 1
print("chuỗi vừa không phải là tiếng anh vừa không phải là số là:", sum)