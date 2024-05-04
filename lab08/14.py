def lst_int(n):
    lst = []
    for a in range(n):
        a = int(input(f" số nguyên thứ {a +1 } : "))
        lst.append(a)
    return lst
n = int(input("số lương: "))
lstbp = lst_int()
binh = list(map(lambda a : a**2, lstbp))
print(f"danh sách các số nguyên a sau khi bình phương là {binh}")