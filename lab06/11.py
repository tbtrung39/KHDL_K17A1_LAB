# tao danh sach a n phantu
n=int(input("moi nhap he so n"))
danh_sach=[]
# gân danh sach
for i in range(n):
    phan_tu=int(input("moi nhap phan tu "))
    danh_sach.append(phan_tu)
# tao dajh sach b 
b=[x for x in danh_sach if x % 3== 0 and x % 5!=  0]
print("danh sach b sau khi duoc tao la:",b)
# # tao danh sach c
c=[x**2 for x in danh_sach]
print("danh sach c sau khi duoc tao la:",c)
# tao danh sach d
d=[x for x in danh_sach if x % 3 ==0 ]
print("danh sach d sau khi duoc tao la:",d)