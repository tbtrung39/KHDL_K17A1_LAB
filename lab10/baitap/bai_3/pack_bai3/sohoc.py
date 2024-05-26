def USCLN(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def BSCNN(a, b):
    return abs(a * b) // USCLN(a, b)
