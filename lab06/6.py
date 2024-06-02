import random
ds=[]
n=1000
for i in range(n):
    random_number=random.randint(1,99999)
    ds.append(random_number)
    print(ds)
for i in range(len(ds)):
    for j in range(i+1,len(ds)):
        if ds[i]>ds[j]:
            ds[i],ds[j]=ds[j],ds[i]
print("danh sách sap xếp:",ds)
C2
ds_sap_xep=sorted(list,reverse=True)