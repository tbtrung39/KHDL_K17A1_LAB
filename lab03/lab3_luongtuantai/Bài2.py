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