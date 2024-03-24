n =  int(input('nhập số n : '))
s1 =0
s2 =1
s3 =0
if n>=0:
    for i in range(1,n+1):
        s1 += i
    for j in range(1,n+1):
        s2 += 2*j+1 
    for k in range(1,n):
        s3 += 2*k
else:
    print("XIn vui lòng nhập lại!!!")

print('S1 = ',s1,'S2 = ',s2,'S3 = ',s3)