import random as r
a=list(input('nhập các số:'))
print(set(r.choices(a,k=r.randint(1,len(a)))))