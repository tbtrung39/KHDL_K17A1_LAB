n=int(input('nhập n:'))
s=0
for i in range(1,n+1):
    s+=i**3
print(f'tổng của {n} số nguyên đầu tiên là:{s}')