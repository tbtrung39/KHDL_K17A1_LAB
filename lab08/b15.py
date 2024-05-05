def binh_phuong_le():
    n=int(input('nhap so gia tri muon nhap:'))
    lst=[]
    for i in range(n):
        a=int(input('nhap so:'))
        lst.append(a)
    print(list(map(lambda x:x**2,list(filter(lambda x: x%2 != 0,lst)))))
binh_phuong_le()