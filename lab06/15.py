tuple=[]
ten=input("nhap ten nguoi dung:")
tuoi=int(input("nhap tuoi:"))
diem=int(input("nhap diem:"))
tuple.append((ten,tuoi,diem))
tuple.sort(key=lambda x:(x[0],x[1],x[2]))
print(tuple)