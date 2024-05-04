def find_ucln(a,b):
    while b!=0:
        a,b=b,a%b
    return a
print(find_ucln(10,15))