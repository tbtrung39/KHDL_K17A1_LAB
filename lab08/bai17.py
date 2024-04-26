from functools import reduce
def tinh_tong_so_chan(n):    
    danh_sach = list(range(1, n+1))   
    so_chan = list(filter(lambda x: x % 2 == 0, danh_sach))
    tong = reduce(lambda x, y: x + y, so_chan, 0)
    return tong

n = int(input("Nhập n: "))
tong_so_chan = tinh_tong_so_chan(n)
print(tong_so_chan)