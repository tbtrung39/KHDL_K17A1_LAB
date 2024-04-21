a=[1,2,3,4]
tu_dien={}
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] + 1 == a[j]:
            tu_dien[i] = j
print(tu_dien)