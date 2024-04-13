list=[]
while True:
    n=int(input("Nhập số tự nhiên:"))
    if n ==0:
        break
    list.append(n)
print(list)
so_duong=[i for i in list if i>0]
so_am=[j for j in list if j<0]
list=so_duong + so_am
print("danh sach khi thay doi: ",list)
m=int(input("nhập giá tri m:"))
list.insert(0,m)
list.append(m)
list.insert(4,m)
print("Danh sach moi",list)