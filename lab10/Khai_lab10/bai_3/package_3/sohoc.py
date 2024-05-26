import math as m
def UCLN(a,b):
    return m.gcd(a,b)

def BCNN(a,b):
    return a*b//UCLN(a,b)

def SumDivisor(n):
    a=0
    for i in range(1,n):
        if n%i==0:
            a+=i
    return a