def lst_int():
    lst = []
    n = int(input("nhap vao so luong so nguyen nhap tu ban phim: "))
    for a in range(n):
        a = int(input(f"nhap vao so nguyen thu {a +1 } tu ban phim: "))
        lst.append(a)
    return  lst
lstlbp = lst_int()
even_n = [i for i in lstlbp if i% 2 != 0]
squared_a = list(map(lambda a: a**2, even_n))
print(f" danh sach cac so nguyen a le sau khi binh phuong la {squared_a}")