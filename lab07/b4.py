lst= [161,182,161,154,176,170,167,171,170,174,
      150,142,148,165,170,178,156,145,149,163,162,159,165,165,170,
      180,155,159,155,153,152,162,180,168,169,168,167,170]
print("nhom co",len(lst),"sinh vien")
print("chieu cao trung binh trong nhom la:",sum(lst)/len(lst))
chieu_cao_khac_nhau=set(lst)
print("chieu cao khac nhau trong nhom la:",chieu_cao_khac_nhau)
print("chieu cao trung binh khi do la:",sum(chieu_cao_khac_nhau)/len(chieu_cao_khac_nhau))