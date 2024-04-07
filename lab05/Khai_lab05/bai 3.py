a=int(input('nhập số:'))
s=''
while a!=0:
    b=a%2
    a//=2
    s+=str(b)
print(s[::-1])