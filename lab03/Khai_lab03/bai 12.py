a='0123456789A BCDEFGHIJK LMNOPQRSTU VWXYZ'
b=input('nhập mã;')
c=0
for i in enumerate(b):
    for j in enumerate(a):
        if i[1]==j[1]:
           c+=(j[0]*2**i[0])
           break
print(f'số kiểm tra mã container {b} là {c%11}')