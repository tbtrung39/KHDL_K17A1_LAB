def binh_phuong():
    n=int(input('nhap so gia tri muon nhap:'))
    lst=[]
    for i in range(n):
        a=int(input('nhap so:'))
        lst.append(a)
    print(list(map(lambda x:x**2,lst)))
binh_phuong()