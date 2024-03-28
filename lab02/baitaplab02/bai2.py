import math
a,b,c = map(float,input("Enter a,b,c:").split())
if a==0:
    if b == 0:
        if c==0:
            print("Phuong trifnh vo so nghiem")
        else:
            print("phuong trinh vo nghiem")
    else:
        print("phuong trinh co mot nghiem duy nhat:",-b/c)
else:
    delta = b**2-4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print("Phuong trinh co 2 nghiem phan biet:",x1,x2)
    elif delta == 0:
        print("phuong trinh co nghiem kep:",-b/2*a)
    else:
        print("phuong trinh vo nghiem")