def tim_so_nho_nhat(a, b, c):
    return min(a, b, c)

def tim_so_lon_nhat(a, b, c):
    return max(a, b, c)

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))

so_nho_nhat = tim_so_nho_nhat(a, b, c)
so_lon_nhat = tim_so_lon_nhat(a, b, c)

print("Số nhỏ nhất trong ba số là:", so_nho_nhat)
print("Số lớn nhất trong ba số là:", so_lon_nhat)
