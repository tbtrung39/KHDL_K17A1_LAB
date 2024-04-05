chuoi = input("Nhập chuỗi: ")
do_dai_lon_nhat = 0
chuoi_con_dai_nhat = ""
do_dai_hien_tai = 1
chuoi_con_hien_tai = chuoi[0]
for i in range(1, len(chuoi)):
    if chuoi[i] == chuoi[i - 1]:
        do_dai_hien_tai += 1
        chuoi_con_hien_tai += chuoi[i]
    else:
        if do_dai_hien_tai > do_dai_lon_nhat:
            do_dai_lon_nhat = do_dai_hien_tai
            chuoi_con_dai_nhat = chuoi_con_hien_tai
        do_dai_hien_tai = 1
        chuoi_con_hien_tai = chuoi[i]
if do_dai_hien_tai > do_dai_lon_nhat:
    do_dai_lon_nhat = do_dai_hien_tai
    chuoi_con_dai_nhat = chuoi_con_hien_tai
print("Chuỗi con dài nhất chứa các ký tự giống nhau là:", chuoi_con_dai_nhat)
