#Yeu cau 1:nguoi dung nhap vao tuple(name,age,score)
thong_tin=[]
while True:
    name=input("Nhap ten(hoac nhap t de thoat):")
    if name=="t":
        break
    age=int(input("Nhap tuoi:"))
    score=float(input("Nhap diem:"))
    thong_tin_tuple=(name,age,score)
    thong_tin.append(thong_tin_tuple)
#Yeu cau 2:Sap xep theo thu tu uu tien ten>tuoi>diem
sap_xep=sorted(thong_tin,key=lambda x: (x[0], x[1], x[2]))

for i in sap_xep:
    name,age,score=i
    print("Ten:",name)
    print("Tuoi:",age)
    print("Diem:",score)
    print("-------------------")