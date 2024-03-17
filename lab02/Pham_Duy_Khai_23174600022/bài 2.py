a=float(input('nhập hệ số a:'))
b=float(input('nhập hệ số b:'))
c=float(input('nhập hệ số c:'))
if a==0:
    print(f'nghiệm của phương trình x={-c/b}')
else:
    delta=b**2-4*a*c
    if delta==0:
        print(f'nghiệm của phương trình là:{-b/(2*a)}')
    elif delta<0:
        print('phương trình vô nghiệm')
    else:
        print(f'phương trình có 2 nghiệm là:\nx1={(-b+pow(delta,1/2))/(2*a)}\nx2={(-b-pow(delta,1/2))/(2*a)}')