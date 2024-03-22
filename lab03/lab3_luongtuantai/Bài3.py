n=int(input('nhập số n:'))
if n==1:
    print('số nguyên tố gần nhất với 1 là:2')
else:
    for i in range(0,n+1):
        a=n
        a+=i 
        for j in range(2,int(pow(a,0.5)+1)):
            if a%j==0:
                break
        else:
            if a==n:
                print(n,'là số nguyên tố')
                break
            else:
                print(f'số nguyên tố gần nhất với {n} là:{a}')
            break
        b=n        
        b-=i
        for k in range(2,int(pow(b,0.5)+1)):
            if b%k==0:
                break
        else:
            if b==n:
                print(n,'là số nguyên tố')
                break
            else:
                print(f'số nguyên tố gần nhất với {n} là:{b}')
            break