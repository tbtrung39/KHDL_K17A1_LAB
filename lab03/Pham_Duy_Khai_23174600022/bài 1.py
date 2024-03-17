n=int(input('nhập số nguyên dương n:'))
s=1
for i in range(0,n+1):
    tich=1
    for j in range(0,i+1):
     a=(2*(j+1))/(2*j+3)
     tich*=a    
    s+=tich
print(f'tổng của dãy số là:{s}')