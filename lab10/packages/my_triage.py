def is_Tam_giac(a,b,c):
    if a+b>c and a+c>b and c+b>a:
        return True
    return False
def chivutamgiac(a,b,c):
    return a+b+c
def S_tangiac(a,b,c):
    s = (a+b+c)/2
    dtich = (s*(s-a)*(s-b)*(s-c))**0.5
    return dtich