so_10 = int(input('Nhập số hệ 10: '))
so_nhi_phan = ''

if so_10 == 0:
    so_nhi_phan = '0'
else:
    while so_10 > 0:
        so_nhi_phan = str(so_10 % 2) + so_nhi_phan
        so_10 //= 2

print('Số nhị phân tương ứng:', so_nhi_phan)
