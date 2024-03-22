n=int(input('nhập giá trị:'))
s1=1
s2=1
s3=1
i=1
while i<=n:
    s1+=pow(-1,i-1)*1/i
    s2+=1/(i*(i+1))
    s3+=1/pow(i+1,0.5)
    i+=1
print(f's1={s1}\ns2={s2}\ns3={s3}')