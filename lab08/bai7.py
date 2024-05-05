def maxmin(a,b,c):
    minabc=min(a,b,c)
    maxabc=max(a,b,c)
    return minabc,maxabc
a=int(input("nhap a : "))
b=int(input("nhap b : "))
c=int(input("nhap c : "))
minabc,maxabc=maxmin(a,b,c)
print("max : ",maxabc)
print("min : ",minabc)