def lst_int():
    list1 = []
    n = int(input("Nhập vào số lượng: "))
    for a in range(n):
        a = int(input(f"Nhập vào số nguyên thứ {a +1 } từ bàn phím: "))
        list1.append(a)
    return list1
lstlbp = lst_int()
so_le = [i for i in lstlbp if i % 2 != 0]
bing_phuong = list(map(lambda a: a**2, so_le))
print(f"Danh sách các số nguyên a lẻ sau khi bình phương là {bing_phuong}")