a=input('nhập chuỗi 1:')
b=input('nhập chuỗi 2:')
s=''
c=max(len(a),len(b))
for i in range(0,c):
    if len(a)>i:
        s+=a[i] 
    if len(b)>i:
        s+=b[i]
print(s)
        
        