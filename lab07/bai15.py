lst=[1,2,3,4,5]
ten=['linh','hoang','dung','tuan','mai']
dct={}
if len(lst)==len(ten):
    for i in range(len(lst)):
        dct[lst[i]]=ten[i]
    print(dct)
else:
    for i in range(len(lst)):
        dct[lst[i]]=ten[i]
    print(dct)