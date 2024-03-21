import math
a= float(input("nhap he so a: "))
b= float(input("nhap he so b: "))
c= float(input("nhap he so c: "))
if a != 0:
    delta=(b*b) - (4*a*c)
    if delta >0:
        print("phuong trinh co 2 nghiem phan biet")
        x1=(-b + math.sqrt(delta))/(2*a)
        x2=(-b - math.sqrt(delta))/(2*a)
        print("x1 =", x1 ,"x2 = ",x2)
    elif delta ==0:
        print("phuong trinh co nghiem duy nhat")
        x=-b/(2*a)
        print("x =",x)
    else:
        print("phuong trinh vo nghiem")
else:
    # bx +c =0
    if b ==0:
        if c==0:
            print("phuong trinh co vo so nghiem")
        else:
            print("phuong trinh vo nghiem")
    else:
        x=-c/b
        print("x =", x)