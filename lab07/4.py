chieu_cao=[161,182,161,154,176,170,150,142,148,165,170,156,156,149,163,162,159,165,165,170,180,155,159,155,153,152,162,160,168,169,168,167,170]
print("tong sinh vien:",len(chieu_cao))
print("chieu cao trung binh cua cac sinh vien:",sum(chieu_cao)/len(chieu_cao))
print("chieu cao khac nhau cua sinh vien:",set(chieu_cao))
print("chieu cao trung binh cua nhom sinh vien:",sum(set(chieu_cao))/len(set(chieu_cao)))