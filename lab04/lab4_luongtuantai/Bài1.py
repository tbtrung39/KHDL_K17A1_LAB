while True:
    n=int(input('nhập giá trị:'))
    if n<=0:
        print('vui lòng nhập giá trị lớn hơn 0!!!')
        continue
    else:
        s4=0
        s5=1
        s6=0
        i=1
        while i<=n:
            s4+=pow(i,2)
            s5+=pow(2*i+1,3)
            s6+=pow(2*i,4)
            i+=1
        print(f's4={s4}\ns5={s5}\ns6={s6}')
        break