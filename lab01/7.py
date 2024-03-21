a=input('Nhap gia tri cua a:')
a=float(a)
b=input('Nhap gia tri cua b:')
b=float(b)
c=input('Nhap gia tri cua c:')
c=float(c)
x=-b/2*a
y=a*((-b/2*a)**2)+b*(-b/2*a)+c
print(f"Dinh cua phuong trinh bac hai la :({x:.2f};{y:.2f})")