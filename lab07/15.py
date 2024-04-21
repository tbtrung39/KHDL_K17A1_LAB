list1 = [1,2,3,4,5,6,7,8,9,10]
list2= ["ten1","ten2","ten3","ten4","ten5","ten6","ten7","ten8","ten9","ten10"]
tu_dien= {list1[i]:list2[i] for i in range(len(list1))}
for so,ten in tu_dien.items():
    print(f"{so}:{ten}")