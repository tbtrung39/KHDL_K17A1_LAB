#Yeu cau 1:Nhap vao danh sach so tu nhien va 0 la dung 
danh_sach=[]
while True:
    phan_tu=int(input("Nhap cac so tu nhien: "))
    if phan_tu == 0:
        break
    danh_sach.append(phan_tu)
#Yeu cau 2: Chen [1,2,3] vao dau cuoi va thu 5 danh sach
danh_sach_chen=[1,2,3]
danh_sach1=danh_sach.copy()
danh_sach1.insert(0,danh_sach_chen)
print("Chen so vao vi tri dau: ",danh_sach1)
danh_sach2=danh_sach.copy()
danh_sach2.insert(-1,danh_sach_chen)
print("Chen so vao vi tri cuoi: ",danh_sach2)
danh_sach3=danh_sach.copy()
danh_sach3.insert(4,danh_sach_chen)
print("Chen so vao vi tri thu 5: ",danh_sach3)
#Yeu cau3: Xoa phan tu thu k ra khoi danh sach
k=int(input("Nhap vi tri muon xoa khoi danh sach(bat dau tu 0): "))
danh_sach4=danh_sach.copy()
del danh_sach4[k]
print(f"Phan tu thu {k} da duoc xoa khoi danh sach")
print("Danh sach truoc khi xoa:",danh_sach)
print("Danh sach sau khi xoa:",danh_sach4)
#Yeu cau4:Sap xep danh sach theo thu tu tang dan, giam dan
danh_sach5=danh_sach.copy()
danh_sach5.sort()
print("Danh sach lon dan la:",danh_sach5)
danh_sach6=danh_sach.copy()
danh_sach6.sort(reverse=True)
print("Danh sach be dan la:",danh_sach6)
