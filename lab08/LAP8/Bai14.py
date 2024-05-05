def lst_int():
    lst = []
    n = int(input("nhập vào số lượng: "))
    for i in range(n):
        i = int(input(f"nhập vào số nguyên thứ {i +1 } từ bàn phím: "))
        lst.append(i)
    return lst
lstbp = lst_int()
binh_phuong = list(map(lambda i : i**2, lstbp))
print(f"danh sách các số nguyên a sau khi bình phương là {binh_phuong}")