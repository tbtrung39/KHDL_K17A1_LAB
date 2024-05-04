#14
def day_so():
    list=[]
    n=int(input("moi nhap so nguyen n"))
    for a in range(n):
        a=int(input("moi nhap so nguyen {n+1}"))
        list.append(a)
    return list
list_bp=day_so()
binh_phong=list(map(lambda a:a**2,list_bp))
print("danh sach sau khi binh phuong la:",binh_phong)
                