a=int(input('nhập số thứ nhất:'))
b=int(input('nhập số thứ hai:'))
#cho a lớn hơn b
if a<b:
    c=a
    a=b
    b=c
i=1
while i<=a:
    d=i*b
    if d%a==0:
        print(f'BCNN của 2 số {a} và {b} là:{d}')
        break
    i+=1