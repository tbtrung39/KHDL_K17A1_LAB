def ucln(a,b):
    if b == 0:
        return a
    return ucln(b,a%b)
def bcnn(a,b):
    return int(a*b/ucln(a,b))
def SumDivisor(n):
    a=sum([i for i in range(1, int(n/2)+1) if n%i==0])
    return a