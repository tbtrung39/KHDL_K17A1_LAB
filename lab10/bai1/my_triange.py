def is_tamgiac(a,b,c):
    if a+b > c and a+c>b and b+c>a:
        return True
    return False
def ChuViTamGiac(a,b,c):
    p= a+b+c
    return p
def S_tam_giac(a,b,c):
    s= (a+b+c)/2
    A = (s*(s-a)*(s-b)*(s-c))
    return A
