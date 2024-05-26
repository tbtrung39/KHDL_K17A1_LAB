def ucln(a,b):
    while b:
        a,b=b,a%b
    return a
def bnln(a,b):
    return abs(a*b)//ucln(a,b)

def sumdivisor(n):
    tong=0
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            tong +=1
            if i!=n//i:
                tong +=n//i
    return tong