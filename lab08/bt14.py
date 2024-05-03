def day_so():
    list = []
    n = int(input("Nhập vào số lượng số nguyên nhập từ bàn phím: "))
    for a in range(n):
        a = int(input(f"Nhập vào số nguyên thứ {a+1} từ bàn phím: "))
        list.append(a)
    return list
list_bp = day_so()
binh_phuong = list(map(lambda a : a**2, list_bp))
print(f"Danh sách các số nguyên a sau khi bình phương là {binh_phuong}")