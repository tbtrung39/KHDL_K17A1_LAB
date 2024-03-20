#Viết chương trình nhập vào các hệ số a, b, c và in ra nghiệm của phương trình bậc hai ax2+ bx + c = 0 (giải và biện luận đầy đủ các trường hợp).
import math
a=int(input("moi nhap a:"))
b=int(input("moi nhap b:"))
c=int(input("moi nhap c:"))

delta=b*b-a*c
if delta>0:
    x1=(-b+delta**0.5)/(2*a)
    x2=(-b-delta**0.5)/(2*a)
    print("phuong trinh co hai nghiem ")
elif delta==0:
    x=b/2*a
    print("phuong trinh co kep")
else:
    print("phuong trinh khong co nghiem")
