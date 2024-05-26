def phuongtrinhbacnhat1an(a,b):
    if a==0:
        if b==0:
            return "phuong trinh vo so nghiem"
        else:
            return "phuong trinh vo nghiem"
    else:
        return -b/a
import math    
def phuongtrinhbac2(a,b,c):
    delta=(b**2) -(4*a*c)
    if delta<0:
        print("phuong trinh vo nghiem")
    elif delta == 0:
        print("phuong trinh co 1 nghiem duy nhat ")
        return -b/(2*a)
    elif delta>0:
        print("phuong trinh co 2 nghiem phan biet")
        print(f" nghiem 1 = ",(-b+ math.sqrt(delta)/(2*a)) )
        print(f"nghiem 2 =", (-b- math.sqrt(delta)/(2*a)))
        