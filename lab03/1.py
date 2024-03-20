n=int(input("moi nhap so n:"))
total=1
result=1
for i in range(0,n+1):
    total*=2*(n+1)*(2*n+3)
    result+=total
    print("ket qua cua phep toan la:",result)
    