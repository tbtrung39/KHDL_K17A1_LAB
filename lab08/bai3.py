import math
def check_int(n):
    for i in range(1,n+1):
        if n % i !=0:
            for j in range(2,int(i**0.5) + 1):
                if i % j == 0:
                    break
            else:
                print(i,end="")
n = int(input("nhập vào số nguyên n: "))
check_int(n)