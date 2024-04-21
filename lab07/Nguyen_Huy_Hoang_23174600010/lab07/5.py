import random as r
while True:
    a=set(r.choices([0,1,2,3,4,5,6,7,8,9],k=5))
    if len(a)==5:
        break
print('tập hợp A:',a)