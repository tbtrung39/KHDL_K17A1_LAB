lst=[]
while True:
    n= int(input("nhap so tu nhien: "))
    if n==0:
        break
    lst.append(n)
lst1 = lst.copy()

list_chen=[1,2,3]
lst.insert(0, list_chen)
lst.append(list_chen)
lst.insert(4,list_chen)
print("list sau khi chen:", lst)

k=int(input("nhap thu tu phan tu muon xoa: "))
lst.pop(k)
print("list da xoa phan tu k:", lst)

lst1.sort()
print("Danh sách tăng dần:", lst1)

lst1.sort(reverse=True)
print("Danh sách giảm dần:", lst1)