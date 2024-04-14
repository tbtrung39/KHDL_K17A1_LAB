import random
import string
#Yeu cau 1:tao danh sach list_ vaf in cac phan tu ra man hinh
list_=[["mon",73],["tue",89],["wed",95],["thu",103],["fri",115],["sat",128],["sun",120]]

for i in list_:
    print(i)

#Yeu cau 2: CHon ra phan tu thu hai, thuoc vi tri thu 3 cua sublist
#Truy cap danh sach con trong danh sach goc
phan_tu= list_[2][1]
print(phan_tu)

#Yeu cau 3: kiem tra do dai cua list test va them mot sublist ngau nhien
list_test= len(list_)
print(list_test)

sublist=[]

chu_cai="".join(random.choices(string.ascii_letters,k=3))
chu_so=random.randint(0,999)

sublist.append(chu_cai)
sublist.append(chu_so)

list_1=list_.copy()
list_1.append(sublist)
print(list_1)
#Yeu cau 4: Thuc hien tinh toan tong sale value trong t2,t3,t7,cn
sale_value=0
for sublist in list_:
    if sublist[0] in ["mon","tue","sat","sun"]:
        sale_value += sublist[1]
print("Tong sale value la:",sale_value)
