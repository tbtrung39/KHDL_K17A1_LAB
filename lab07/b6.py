n = int(input("nhập vào số tự nhiên n: "))
for i in range(1,n+1):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i,end = " ")