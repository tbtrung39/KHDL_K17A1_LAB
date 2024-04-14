import random as r
a=[]
for i in range(0,201):
    if i%5==0 and i%7==0:
        a.append(i)
print(r.randint(a))