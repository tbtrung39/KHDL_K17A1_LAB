n=-1
while (n<=0):
    n = int(input("enter in interger:"))
ketqua=""
while (n/2>0):
    ketqua= str(n%2)+ketqua
    print("n%2=",n%2)
    n=n//2
    print("n=",n)
print(ketqua)