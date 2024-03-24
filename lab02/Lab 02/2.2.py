'''
Viết chương trình nhập vào các hệ số a, b, c và in ra nghiệm của phương trình bậc hai ax^2+ bx + c = 0 
'''
# VIET PHUONG TRINH NHAP VAO CAC HE SO a,b,c
# cua phuong trinh bac 2 ax^2 + bc + c = 0
# tim nghiem cua phuong trinh

a = int(input("nhap vao gia tri a:"))
b = int(input("nhap vao gia tri b:"))
c = int(input("nhap vao gia tri c:"))
delta = b**2 - 4*a*c
if delta > 0:
    x1 = (-b + delta**0.5) / (2*a)
    x2 = (-b - delta**0.5) / (2*a)
    print(x1)
    print(x2)
elif delta == 0:
    x3 = (-b) / (2*a)
    print(x3)
else:
    print("Phuong  trinh vo nghiem")