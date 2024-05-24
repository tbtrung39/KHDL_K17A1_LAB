def ucln(a, b):
    while b:
        a,b=b,a%b
    return a
def bcnn(a, b):
    return abs(a*b)//ucln(a,b)
def sumDivisor(n):
    total=0
    for i in range(1,n+1):
        if n%i==0:
            total+=i
    return total
