from functools import reduce

n = int(input('nhap n : '))
ds = [i for i in range(1, n + 1)]

list_moi = list(filter(lambda x: x % 2 == 0, ds))
tong = reduce(lambda x, y: x + y, list_moi)
print('tong cac so chan trong danh sach da nhap la : ', tong)
