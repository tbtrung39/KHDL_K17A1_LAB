n=int(input('nhập số n:'))
s=0
for i in range(1,n+1):
    s+=pow(i,3)
print(f'tổng bậc 3 của {n} số nguyên đầu tiên là:',s)