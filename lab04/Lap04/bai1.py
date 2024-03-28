
n=int(input('Nhập giá trị n:'))
while True:
    if n<=0:
        print('Nhập lại')
    else:
        break
# a
i=1
s4=0
while i<=n:
    s4+= i**2
    i+=1
print(s4)
# b
i=1
s5=0
while i<=n:
    s5 += (2*i+1)**3
    i+=1
print(s5)