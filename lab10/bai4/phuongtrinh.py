def bac_nhat(a,b):
    if a ==0:
        if b==0:
            print("phuong trinh co vo so nghiem")
        else:
            print("phuong trinh vo nghiem")
    else:
        x = -b/a
        print("nghiem cua phuong trinh la: ",x)
    return x
def bac_hai(a,b,c):
    print("phuong trinh bac 2 ")
    if a ==0:
        if b ==0:
            if c ==0 :
                print("phuong trinh co vo so nghiem:")
            else:
                print("phuong trinh vo nghiem")
        else:
            x= -c/b
            print("phuong trinh co nghiem duy nhat x=",x)
            return x
    else:
        delta = b**2 - 4*a*c
        if delta >0:
            x1 = (-b + delta**0.5)/(2*a)
            x2 = (-b - delta**0.5)/(2*a)
            print("x1 =",x1)
            print("x2 =",x2)
            return x1,x2
        else:
            if delta == 0:
                x= -b/(2*a)
                print("phuong trinh co nghiem kep x=",x)
                return x
            else:
                print("phuong trinh vo nghiem")