import random
#cach 1
lst=[random.randint(1,99999) for i in range(1000)]
ds_sap_xep=sorted(lst)
print("danh sach da sap xep la:", ds_sap_xep)

#cach 2
lst=[random.randint(1,99999) for i in range(1000)]
for i in range(len(lst)):
    for j in range(len(lst)-1):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
print("danh sach da sap xep la:", lst)