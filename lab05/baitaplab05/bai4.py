a = input()
b = input()
c=max(len(a),len(b))
s=''
for i in range(0,c):
    if i<len(a):
        s+=a[i]
    if i<len(b):
        s+=b[i]
print(s)