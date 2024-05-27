def ucln(a,b):
    while b != 0:
        a, b = b, a%b
    return a

def bcnn(a,b):
    a_goc = a
    b_goc = b
    while a != b:
        if a < b:
            a += a_goc
        else: 
            b += b_goc
    return a