#1
#a
a=[2,-4,1,9,-3,6,3,2,6,8]
tong=0
for i in a:
    tong+=i
print(tong)
#b
a=[2,-4,1,9,-3,6,3,-2,6,8]
tong=0
for i in a:
    if i >0:
        tong+=i
print(tong)
#c
a=[2,-4,1,9,-3,6,3,-2,6,8]
for index, i in enumerate(a) :
    if i<0:
        print(index)
        break
#d
a=[2,-4,1,9,-3,6,3,-2,6,8]
for index in range(len(a) - 1, -1, -1):
    if a[index]>0:
        print(index)
        break
#e
a=[2,-4,1,9,-3,6,3,-2,6,8]
for index, i in enumerate(a,-1) :
    if a[index]>0:
        print(index)
        break
#f
a=[2,-4,1,9,-3,6,3,-2,6,8]
max=max(a)
vitri=None
for index,i in enumerate(a):
    if i==max:
        vitri=index
print(" số lớn nhất = ",max )
print(" vị trí = " ,vitri)