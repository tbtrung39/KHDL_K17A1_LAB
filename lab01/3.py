pi=3.14
r=input("Nhap ban kinh cua hinh tru :")
r=float(r)
h=input("Nhap chieu cao cua hinh tru :")
h=float(h)
xq= 2*pi*r*h
tp=2*pi*r*(r+h)
tt=pi*r**2*h
print(f"Diện tích xung quanh của hình trụ là: {xq:.2f}")
print(f"Diện tích toàn phần của hình trụ là: {tp:.2f}")
print(f"Thể tích của hình trụ là: {tt:.2f}")