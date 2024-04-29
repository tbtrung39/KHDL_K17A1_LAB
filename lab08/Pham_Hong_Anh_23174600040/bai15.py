def lst_int(n):
    lst = []
    for a in range(n):
        a = int(input(f" số nguyên thứ {a +1 } : "))
        lst.append(a)
    return lst
n = int(input("số lương: "))
lstlbp = lst_int()
even_n = [i for i in lstlbp if i % 2 != 0]
binh = list(map(lambda a: a**2, even_n))
print(f"danh sách các số nguyên a lẻ sau khi bình phương là {binh}")