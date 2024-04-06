chuoi = input("Nhap chuoi ky tu : ")
max_chuoi_con = ""
current_chuoi_con = chuoi[0]
for i in range(1, len(chuoi)):
    if chuoi[i] == chuoi[i - 1]:
        current_chuoi_con += chuoi[i]
    else:
        if len(current_chuoi_con) > len(max_chuoi_con):
            max_chuoi_con = current_chuoi_con
            current_chuoi_con = chuoi[i]
print(max_chuoi_con)