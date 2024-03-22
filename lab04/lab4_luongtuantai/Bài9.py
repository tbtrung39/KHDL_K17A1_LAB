a=input('nhập số:')
i=0
s=0
while i<len(a):
    b=int(a[i])
    s+=b
    i+=1
print(f'tổng các chữ số của số {a} = {s}')
