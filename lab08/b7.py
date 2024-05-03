def so_nho_nhat(a,b,c):
    so_nho_nhat=min(a,b,c)
    return so_nho_nhat
def so_lon_nhat(a,b,c):
    so_lon_nhat=max(a,b,c)
    return so_lon_nhat
a=int(input("Nhập số a: "))
b=int(input("Nhập số b: "))
c=int(input("Nhập số c: "))
max=so_lon_nhat(a,b,c)
print("Số lớn nhất là: ",max)
min=so_nho_nhat(a,b,c)
print('Nhập số nhỏ nhất: ',min)