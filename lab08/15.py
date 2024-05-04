#15
def day_so():
    list=[]
    n=int(input("moi nhap so nguyen n:"))
    for a in range(n):
        a=int(input("moi nhap so nguyen {n+1}"))
        list.append(a)
    return list
list_bp=day_so()
so_le=[i for i in list_bp if i%2!=0]
binh_phuong=list(map(lambda a:a**2,so_le))
print("nhung so le nam trong day list binh phuong la:",binh_phuong)