a='0123456789ABCDEF'
b=input('nhập chuỗi:')
c=''
for i in b:
    for j in a:
        if i==j:
           c+=i
print(c)
c=c[::-1]
d=0
for i in enumerate(c):
    for j in enumerate(a):
        if i[1]==j[1]:
            d+=j[0]*(16**i[0])
print(d)