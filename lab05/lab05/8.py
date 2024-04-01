chuoi = input("Nhập chuỗi ký tự: ")
chuoi_con_max = ""
do_dai_max = 0
for i in range(len(chuoi)):
    chuoi_con = chuoi[i]
    do_dai = 1
    for j in range(i + 1, len(chuoi)):
        if chuoi[j] == chuoi[i]:
            chuoi_con += chuoi[j]
            do_dai += 1
        else:
            break
    if do_dai > do_dai_max:
        chuoi_con_max = chuoi_con
        do_dai_max = do_dai
print("Chuỗi ký tự con có độ dài cực đại chỉ chứa các ký tự giống nhau là:", chuoi_con_max)
