str = input("Nhập chuỗi: ")
max_chuoi_con = ""
current_chuoi_con = str[0]
for i in range(1, len(str)):
    if str[i] == str[i - 1]:
        current_chuoi_con += str[i]
    else:
        if len(current_chuoi_con) > len(max_chuoi_con):
            max_chuoi_con = current_chuoi_con
            current_chuoi_con = str[i]
print(max_chuoi_con)