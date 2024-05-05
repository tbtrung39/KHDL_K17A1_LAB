def nguyento(a):
    if a <=1 :
        return False
    for i in range(2,int(a**0.5)+1):
        if a % i ==0:
            return False
    return True
def nguyentonhohon(n):
    print("so nguyen to nho hon n la : ")
    for a in range(2,n):
        if nguyento(a):
            print(a,end=" ")
n=int(input("nhap so nguyen duong n: "))
print(nguyentonhohon(n))