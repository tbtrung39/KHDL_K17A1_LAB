n=int(input('nhập số n:'))
if n<2:
    print('không có số nguyên tố nào')
else: 
 print('số nguyên tố là:',end='')
 for i in range(2,n):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=' ')
        