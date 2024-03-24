
n=int(input("Nhậpp cạnh tgiac:"))
for i in range(0,n):  
        if i == n - 1: 
            print('*' * (2 * n - 1))
        else:   
            print(' ' * (n - i - 1) + '*' + ' ' * (2 * i - 1) 
                  + ('*' if i > 0 else ''))