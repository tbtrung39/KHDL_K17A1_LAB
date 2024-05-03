def day_so():
    list = []
    n = int(input("Nhập vào số lượng số nguyên nhập từ bàn phím: "))
    for a in range(n):
        a = int(input(f"Nhập vào số nguyên thứ {a +1 } từ bàn phím: "))
        list.append(a)
    return list
list_bp = day_so()
so_le = [i for i in list_bp if i % 2 != 0]
binh_phuong_so_le = list(map(lambda a: a**2, so_le))
print(f"Danh sách các số nguyên lẻ sau khi bình phương là {binh_phuong_so_le}")