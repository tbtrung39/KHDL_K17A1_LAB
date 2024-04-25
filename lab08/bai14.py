def lst_int():
    lst = []
    n = int(input("nhập vào số lượng số nguyên nhập từ bàn phím: "))
    for a in range(n):
        a = int(input(f"nhập vào số nguyên thứ {a +1 } từ bàn phím: "))
        lst.append(a)
    return lst
lstbp = lst_int()
squared_a = list(map(lambda a : a**2, lstbp))
print(f"danh sách các số nguyên a sau khi bình phương là {squared_a}")