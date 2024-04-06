str=input('Nhap ki tu chuoi:')
so=''
for c in str:
    if c.isdigit():
        so+=str(c)
if so: 
    n=int(so)
    print('Chuoi so:',so)
    tong=0
    for i in range(1,n):
        if n%i==0:
            tong+=i
        if tong==so:
            print('la so hoan hao',so)
        else:
            print('khong phai so haon hao',so)
else:
    print('CHUOI NHAP KHONG CHUA SO')