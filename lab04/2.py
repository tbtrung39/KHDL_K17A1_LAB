## tính tổng 


while True:
    n =  int(input('nhập vào số nguyên dương  ở đây :'))
    if n <=0:
        print('nhập số lớn hơn  không ')
        continue
    else:
        s1 =0
        i  =  1
        s2 =0
        s3 =0
        while i<=n :
            s1 = s1 +(1/i)
            s2 = s2 + 1/(i*(i+1))
            s3  =  s3 + 1/pow(i+1,0,5)
            i = i+1
        print('tổng s ở câu a là : ',s1,'\n',
            'tổng s ở câu b là : ',s2,'\n',
            'tổng s ở câu c là : ',s3,'\n')
        break
            