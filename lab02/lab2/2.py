#Viết chương trình nhập vào các hệ số a, b, c và in ra nghiệm của phương trình bậc hai ax^2+ bx + c = 0 
a=int(input("nhập vào số a:"))
b=int(input("nhập vào số b:"))
c=int(input("nhập vào số c:"))
delta=b**2-4*a*c
if delta>0:
    x1=(-b+delta**0.5)/(2*a)
    x2=(-b-delta**0.5)/(2*a)
    print(x1)
    print(x2)
if delta==0:
    x3=(-b)/(2*a)
    print(x3)
else:
    print("phương trình vô nghiệm")
