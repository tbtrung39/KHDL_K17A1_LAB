while True:
    n =  int(input('nhập vào số nguyên dương  ở đây :'))
    if n <=0:
        print('nhập số lớn hơn  không ')
        continue
    else:
        s4 =0
        s5=1
        s6=0
        i =1 
        while i<=n:
            s4 +=pow(i,2)
            s5 +=pow(2*i+1,3)
            s6 +=pow(2*i,4)
            i = i+1
        print('s4 =',s4,'s5 = ',s5,'s6 = ',s6)
        break
        