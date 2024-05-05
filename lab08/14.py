def lst_int():
    lst = []
    n = int(input("nhap vao so luong so nguyen nhap tu ban phim: "))
    for a in range(n):
        a = int(input(f"nhap vao so nguyen thu {a +1} tu ban phim: "))
        lst.append(a)
    return lst
lstbp = lst_int()
squared_a = list(map(lambda a : a**2, lstbp))
print(f"danh sach cac so nguyen a sau khi binh phuong la {squared_a}")