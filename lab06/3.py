#3
danh_sach=[]
while True:
    phan_tu=int(input('moi nhap phan tu:'))
    danh_sach.append(phan_tu)
    if phan_tu==0:
        print("krt thuc chuon trinh")
        break

#chen phan tu m
m=int(input("moi nhap phan tu m:"))
# chen m vao dau danh sach
danh_sach.insert(0,m)
# chen m vao cuoi danh sach
danh_sach.append(m)
# chen m vao vi tri thu 5
danh_sach.insert(4,m)
print("thu tu cac phan tu m duoc them vao la:",danh_sach)