def so_lon_nhat(a,b,c):
    return max( a,b,c)
def so_nho_nhat( a,b,c):
    return min (a ,b,c)
a = int(input('Nhập a:'))
b = int(input('Nhập b:'))
c = int(input('Nhập c:'))
lon_nhat =  so_lon_nhat(a,b,c)
nho_nhat = so_nho_nhat(a,b,c)
print(f'Số lớn nhất là: {lon_nhat}')
print(f'Số nhỏ nhất là: {nho_nhat}')
