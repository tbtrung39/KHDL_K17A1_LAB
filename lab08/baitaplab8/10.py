def uoc(n):
    for i in (1,n):
        if n%i==0:
            print(i)
n = int(input("Nhập n:"))
while n<=0:
    n = int(input("Please enter positive number:"))
uoc(n)