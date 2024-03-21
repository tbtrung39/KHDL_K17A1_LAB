#Viết chương trình in ra màn hình học lực của học sinh theo thang điểm như sau:
diem_tk=int(input("moi nhap so diem:"))
if (diem_tk>=0) or (diem_tk<=3):
     print("hoc sinh la hoc sinh loai kem")
elif diem_tk==4.0:
      print("hoc sinh la hoc sinh xep loai yeu.25")
elif (diem_tk>=5) or (diem_tk<=6):
      print("hoc sinh xep loai trung binh:")
elif (diem_tk>=7) or (diem_tk<=8):
      print("hoc sinh xep loai kha:")
elif (diem_tk>=9) or (diem_tk<=10):
      print("hoc sinh xep loai gioi:")
else:
      print("khong co so diem nao thoa man")