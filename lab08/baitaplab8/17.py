from functools import reduce
def so_chan(n):
    return n%2==0
def tinh_tong(a1,b1):
    return a1+b1
n = int(input("Nhập giá trị từ bàn phím:"))
lst = list(range(1,n+1))
tong_so_chan = reduce(tinh_tong,filter(so_chan,lst))
print(tong_so_chan)