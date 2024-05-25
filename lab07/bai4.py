thong_ke_chieu_cao=(161,182,161,154,176,170,167,171,170,174,150,142,148,165,170,178,156,145,149,163,162,159,165,165,170,180,155,159,155,152,162,180,168,169,168,167,170)
print("so sinh vienla: ",len(thong_ke_chieu_cao))
print("chieu cao trung binh cua sinh vien: ", sum(thong_ke_chieu_cao)/ len(thong_ke_chieu_cao))
thong_ke_chieu_cao_khac_nhau=set(thong_ke_chieu_cao)
for i in thong_ke_chieu_cao_khac_nhau:
    print(i)
trung_binh= sum(thong_ke_chieu_cao_khac_nhau)/len(thong_ke_chieu_cao_khac_nhau)
print(trung_binh)