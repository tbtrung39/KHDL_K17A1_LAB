# câu 1
n=int(input('nhập số nguyên dương n:'))
s=1
for i in range(0,n+1):
    tich=1
    for j in range(0,i+1):
     a=(2*(j+1))/(2*j+3)
     tich*=a    
    s+=tich
print(f'tổng của dãy số là:{s}')

# câu 2
n=int(input('nhập số n:'))
if n<6:
    print('không có số hoàn hảo nào')
else:  
    print('số hoàn hảo:',end='')  
    for i in range(1,n):
        s=0    
        for j in range(1,i):
            if i%j==0:
                s+=j
        if s==i:
            print(i, end=' ')

# câu 3
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

# câu 4
n=int(input('nhập số n:'))
if n<2:
    print('không có số nguyên tố nào')
else: 
 print(f'các số nguyên tố bé hơn {n} là:',end='')
 for i in range(2,n):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=' ')

# câu 5
m = int(input("Nhập chiều dài: "))
n = int(input("Nhập chiều rông: "))
for i in range(n):
    for j in range(m):
        print("*", end ='')
    print("\r")

# câu 6
n=int(input('nhập n:'))
s=0
for i in range(1,n+1):
    s+=i**3
print(f'tổng của {n} số nguyên đầu tiên là:{s}')

# câu 7
n=int(input('nhập n:'))
s=0
for i in range(1,n+1):
    s+=i**3
print(f'tổng của {n} số nguyên đầu tiên là:{s}')

# câu 8

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

# câu 9
n=int(input('nhập n:'))
if n<=0:
    print('nhập số lớn hơn bằng 0!!!')
else:
    s4=0
    s5=0
    s6=0
    for i in range(0,n+1):
        s4+=i**2
        s5+=(2*n+1)**3
        s6+=(2*n)**4
    print('s4=',s4)
    print('s5=',s5)
    print('s6=',s6)

# câu 11
h=int(input('nhập chiều cao của tam giác cân:'))
print("tam giác a")
k=2*h-2
n=0
for dong in range(1,h+1):
    for cot in range(1,k+1):
        print(end=' ')
    
    if dong==1:
        print('*',end=' ')
    elif dong!=1 and dong!=h:  
        print('*',end=' ')
        for i in range(0,n):
            print(end=' ')
        print('*',end=' ')
        n+=2
        j=(n+4)//2
    elif dong==h:
     for cot in range(1,j*2):
        print('*',end='')
     print(end=' ')

    k=k-1
    print('\r')

print('tam giác b')
k=2*h-2
n=2
for dong in range(1,h+1):
    for cot in range(1,k+1):
        print(end=' ')
    if dong==1:
        print(' *',end=' ')
    elif dong!=1 and dong!=h:  
        print('*',end=' ')
        for i in range(0,n):
            print(end=' ')
        print('*',end=' ')
        n+=2
        j=(n+4)//2
    elif dong==h:
     n-=2
     for cot in range(1,j):
        print('* ',end='')
     print('*',end=' ')
    k=k-1
    print('\r') 
    
print('tam giác c')
k=2*h-2
for dong in range(1,h+1):
    for cot in range(1,k+1):
        print(end=' ')
    for cot in range(1,dong+1):
        print('*',end=' ')
    k=k-1
    print('\r')

# câu 12 
a='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def tri_so(n):
 for i in enumerate(a):
    if i[1]==n:
        if i[0]%11==0:
            return i[0]+1
        else:
            return i[0]

print(tri_so("Z"))