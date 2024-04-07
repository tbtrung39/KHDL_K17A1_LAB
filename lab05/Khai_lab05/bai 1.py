a=input('nhập chuỗi bất kì:')
s=0
for i in a:
    if i.isdigit():
        s+=1
print('số kí tự là số trong chuỗi là:',s)
