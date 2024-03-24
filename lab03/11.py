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