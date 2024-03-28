n=int(input('Nhập một số:'))
print(f'Các số hoàn hảo nhỏ hơn {n} là:')
for num in range(2,n):
    sum=1
    for i in range(2,num):
        if num % i ==0:
            sum +=i
    if sum == num:
        print(num)