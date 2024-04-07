a=input('nhập chuỗi:')
for i in a:
    if not(i.isdigit()):
        a=a.replace(i,'')
a=int(a)
s=0
for i in range(1,a):
    if a%i==0:
        s+=i
if s==a:
    print(a,'là số hoàn hảo')
else:
    print(a,'không là số hoàn hảo')