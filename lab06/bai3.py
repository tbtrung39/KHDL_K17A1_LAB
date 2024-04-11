list=[]
while True:
    n= int(input("nhap so tu nhien: "))
    if n==0:
        break
    list.append(n)

duong=[x for x in list if x>0]
am=[x for x in list if x<0]
ket_qua=duong +am
print(ket_qua)

m=int(input("nhap so can chen vao danh sach: "))
list.insert(0,m)
list.append(m)
list.insert(4,m)
print("list sau khi chen: ",list)