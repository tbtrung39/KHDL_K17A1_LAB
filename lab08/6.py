def find_ucln(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def shorten_fraction(a,b):
    return (a*b)//find_ucln(a,b)
a1 = int(input("Enter first number:"))
a2 = int(input("Enter second number:"))
bcnn = shorten_fraction(a1,a2)
print(f"Bội chung nhỏ nhất là:{bcnn}")