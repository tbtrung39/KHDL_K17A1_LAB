def tim_so_nho_nhat(a, b, c):
    return min(a, b, c)
def tim_so_lon_nhat(a, b, c):
    return max(a, b, c)
a = int(input("Nhap so nguyen thu nhat: "))
b = int(input("Nhap so nguyen thu hai: "))
c = int(input("Nhap so nguyen thu ba: "))
so_nho_nhat = tim_so_nho_nhat(a, b, c)
so_lon_nhat = tim_so_lon_nhat(a, b, c)
print("So nho nhat la:", so_nho_nhat)
print("So lon nhat la:", so_lon_nhat)
