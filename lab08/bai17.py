from functools import reduce

def la_so_chan(x):
    return x % 2 == 0

def tinh_tong(lst):
    return reduce(lambda x, y: x + y, lst)

n = int(input("Nhập giá trị của n: "))
danh_sach = list(range(1, n + 1))
so_chan = list(filter(la_so_chan, danh_sach))
tong_so_chan = tinh_tong(so_chan)

print("Danh sách các số chẵn từ 1 đến", n, ":", so_chan)
print("Tổng các số chẵn từ 1 đến", n, ":", tong_so_chan)
