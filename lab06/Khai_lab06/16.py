x=int(input('nhập hàng:'))
y=int(input('nhập cột:'))
a=[]
for i in range(0,x):
    b=[]
    for j in range(0,y):
        b.append(i*j)
    a.append(b)
print(a)