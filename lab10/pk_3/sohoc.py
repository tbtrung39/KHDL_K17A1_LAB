def UCLN(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def BCNN(a, b):
    return abs(a * b) // UCLN(a, b)
