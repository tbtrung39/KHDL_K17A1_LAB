def find_ucln(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def shorten_fraction(tu_so,mau_so):
    ucln = find_ucln(tu_so,mau_so)
    return tu_so//ucln,mau_so//ucln
tu_so = int(input("Enter numerator:"))
mau_so = int(input("Enter denomirator:"))
tu_so1,mau_so1=shorten_fraction(tu_so,mau_so)
print(f"Fraction after reducetion:{tu_so1}/{mau_so1}")