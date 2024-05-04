#10
def uoc_so(n):
    uoc=[]
    for i in range(1,n+1):
        if n%i==0:
            uoc.append(i)
    return uoc
n=int(input("moi nhap he so n:"))
uoc_so(n)
print("uoc so cua n la:",uoc_so(n))