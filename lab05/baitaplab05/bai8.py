str = input("Nhập chuỗi ký tự là: ")
max_chuoi = ""
chuoi_con = str[0]
for i in range(1, len(str)):
    if str[i] == str[i - 1]:
        chuoi_con += str[i]
    else:
        if len(chuoi_con) > len(max_chuoi):
            max_chuoi = chuoi_con
            chuoi_con = str[i]
print(max_chuoi)

