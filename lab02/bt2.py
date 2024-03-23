a=int(input('Nhập giá trị a:'))
b=int(input('Nhập giá trị b:'))
c=int(input('Nhập giá trị c:'))
delta=b**2-4*a*c
if delta >0:
    x1=(-b+delta**0.5)/(2*a)
    x2=(-b-delta**0.5)/(2*a)
    print(x1)
    print(x2)
elif delta ==0:
    x3=(-b)/(2*a)
    print(x3)
else:
    print('Phương trình vô nghiệm.')