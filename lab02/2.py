#Viết chương trình nhập vào các hệ số a, b, c và in ra nghiệm của phương trình bậc hai ax^2+ bx + c = 0 
import math
a=int(input("moi nhap so a"))
b=int(input("moi nhap so b"))
c=int(input("moi nhap so c"))
 
delta=b*b-4*a*c
if delta > 0:
    x1= (-b+delta**0.5)/(2*a)
    x2= (-b-delta**0.5)/(2*a)
    print("phuong trinh co hai nghiem phan biet:")
elif delta==0:
    x3=-b/2*a
    print("phuong trinh nghiem thuc kep")
else:
    print("phuong trinh vo nghiem")