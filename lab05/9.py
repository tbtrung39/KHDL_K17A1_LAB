chuoi1=input("Nhap chuoi1:")
chuoi2=input("Nhâkp chuôi2:")
ki_tu_chung=""
for i in range(len(chuoi1)):
  for j in chuoi2:
    if chuoi1[i]==j:
      ki_tu_chung+=j
      print("Kí tự chung:",ki_tu_chung)

