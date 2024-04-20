a=[1,2,3,4]
dic={}
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]+1==a[j]:
            dic[i]=j
print(dic)