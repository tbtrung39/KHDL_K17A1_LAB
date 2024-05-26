def kiemtratamgiac(a,b,c):
    if a+b>c and b+c>a and a+c>b:
        return True 
    else:
        return False
    
def chuvitamgiac(a,b,c):
    return a+b+c

def S_tamgiac(a,b,c):
    p=(a+b+c)/2
    return (p*(p-a)*(p-b)*(p-c))**(1/2)