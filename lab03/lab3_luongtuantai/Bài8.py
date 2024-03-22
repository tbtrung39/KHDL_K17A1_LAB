n=int(input('nhập n:'))
if n<=0:
    print('nhập số lớn hơn 0!!!')
else:
    s1=0
    s2=0
    s3=0    
    for i in range(0,n+1):
        s1+=i
        s2+=(2*n+1)
        s3+=(2*n)
    print('S1=',s1)
    print('S2=',s2)
    print('S3=',s3)