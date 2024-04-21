chieu_cao=[161,182,161,154,176,170,167,171,170,174,150,142,148,165,
           170,178,156,145,149,163,162,159,165,165,170,180,155,159,
           155,153,152,162,180,168,167,170]
#Nhom co bao nhieu sinh vien
so_luong_sv=len(chieu_cao)
print("So luong sinh vien trong nhom la:",so_luong_sv)
#Chieu cao trung binh cua cac sinh vien
trung_binh=sum(chieu_cao)/so_luong_sv
print("Chieu cao trung binh cua nhom la:",trung_binh)
#Liet ke cac chieu cao khac nhau
chieu_cao_khac_nhau=set(chieu_cao)
print("Liet ke cac chieu cao cua nhom la:",chieu_cao_khac_nhau)