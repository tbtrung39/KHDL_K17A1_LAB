from pk3 import uoc, uoc_chung_lon_nhat, boi_chung_nho_nhat

a = int(input("nhap a: "))
b = int(input("nhap b: "))
n = int(input("nhap n: "))

print("ucln:", uoc_chung_lon_nhat(a, b))
print("bcnn:", boi_chung_nho_nhat(a, b))
print("cac uoc cua", n, "la:", uoc(n))
