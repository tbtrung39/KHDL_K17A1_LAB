#C
n = int(input("nhap so hang: "))
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print("",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print()
#b
for i in range(1,n):
    for j in range(1,n+1-i):
        print("",end=" ")
    for k in range(1,i+1):
        if k ==1 or k ==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for k in range(1,n+1):
    print("*",end=" ")
print()
#a em khong lam duoc