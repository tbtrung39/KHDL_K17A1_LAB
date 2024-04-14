#Yeu cau 1:Nhap vao danh sach so tu nhien va 0 la dung 
danh_sach=[]
while True:
    phan_tu=int(input("Nhap cac so tu nhien: "))
    if phan_tu == 0:
        break
    danh_sach.append(phan_tu)
#Yeu cau 2:Chuyen phan tu duong len dau danh sach va in ra
danh_sach_moi=[]
for i in danh_sach:
    if i>0:
        danh_sach_moi.insert(0,i)

print(danh_sach_moi)
#Yeu cau 3: Chen m vao dau cuoi va thu 5 danh sach
m=int(input("Nhap so muon chen vao danh sach: "))
danh_sach1=danh_sach.copy()
danh_sach1.insert(0,m)
print("Chen so vao vi tri dau: ",danh_sach1)
danh_sach2=danh_sach.copy()
danh_sach2.insert(-1,m)
print("Chen so vao vi tri cuoi: ",danh_sach2)
danh_sach3=danh_sach.copy()
danh_sach3.insert(4,m)
print("Chen so vao vi tri thu 5: ",danh_sach3)