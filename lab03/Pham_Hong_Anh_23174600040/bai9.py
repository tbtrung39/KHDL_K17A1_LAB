n=int(input('nhập n:'))
if n<=0:
    print('nhập số lớn hơn bằng 0!!!')
else:
    s4=0
    s5=0
    s6=0
    for i in range(0,n+1):
        s4+=i**2
        s5+=(2*n+1)**3
        s6+=(2*n)**4
    print('s4=',s4)
    print('s5=',s5)
    print('s6=',s6)