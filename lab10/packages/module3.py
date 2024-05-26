import math
def ucln(a,b):
    while b:
        a, b = b, a % b
    return a
    
def bcnn(a,b):
    bc = abs(a * b) // math.gcd(a,b)
    return bc
