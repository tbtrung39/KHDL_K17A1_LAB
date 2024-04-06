str = input("Nhập chuỗi ký tự: ")
chuoi_ki_tu = ""
chuoi_con = str[0]
for i in range(1,len(str)):
    if str[i] == str[i-1]:
        chuoi_con += str[i]
    else:
        if len(chuoi_con) > len(chuoi_ki_tu):
            chuoi_ki_tu = chuoi_con
            chuoi_con = str[i]
print("Chuỗi kí tự in ra: ",chuoi_ki_tu)
