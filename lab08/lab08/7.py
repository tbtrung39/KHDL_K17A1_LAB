def tim_so_lon_nhat(a, b, c):
    return max(a, b, c)

def tim_so_nho_nhat(a, b, c):
    return min(a, b, c)
a = int(input("nhap so nguyen thu nhat: "))
b = int(input("nhap so nguyen thu hai: "))
c = int(input("nhap so nguyen thu ba: "))
so_lon_nhat = tim_so_lon_nhat(a, b, c)
so_nho_nhat = tim_so_nho_nhat(a, b, c)
print("so lon nhat la:", so_lon_nhat)
print("so nho nhat la:", so_nho_nhat)
