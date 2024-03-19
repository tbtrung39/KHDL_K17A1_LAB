a=int(input("nhập giá trih thứ nhất: "))
b=int(input("nhập giá trih thứ hai: "))
c=int(input("nhập giá trih thứ ba: "))

if a==0:
    x=(-c)/b
    print("nghiệm của phương trình là:",x )
delta=b**2-4*a*c
if delta >0:
    x1=(-b+delta*0.5)/(2*a)
    x2=(b+delta*0.5)/(2*a)
    print("phương trình có 2 nghiệm phân biệt x1, x2 lần lượt là:", x1, x2)
if delta==0:
    x3= -b/2*a
    print("phương trình có nghiệm duy nhất là:", x3)
if delta<0:
    print("phương trình vô nghiệm")