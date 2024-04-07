chuoi = input("Nhập chuỗi ký tự: ")
chuoi_dai_nhat = ''
chuoi_hien_tai = ''
ki_tu_hien_tai = None
for ki_tu in chuoi:
    if ki_tu == ki_tu_hien_tai:
        chuoi_hien_tai += ki_tu
    else:
        chuoi_hien_tai = ki_tu
        ki_tu_hien_tai = ki_tu
    if len(chuoi_hien_tai) > len(chuoi_dai_nhat):
        chuoi_dai_nhat = chuoi_hien_tai
print("Chuỗi con có độ dài cực đại và chỉ gồm các ký tự giống nhau:", chuoi_dai_nhat)
