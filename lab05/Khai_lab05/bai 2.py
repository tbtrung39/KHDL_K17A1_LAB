a=input('nhập chuỗi bất kì:')
s=0
for i in a:
    if not(i=='w' or i=='z' or i=='f' or i=='j' or i.isdigit()):
        s+=1
print('kí tự không là chữ cái tiếng anh và không là số trong chuỗi là:',s)
        
        