#câu c
n = int(input("Nhập vào chiều cao:"))
k = 2*n-2
for i in range(0,n+1):
    for a in range(0,k+1):
        print(end=' ')
    k-=1
    for a in range(0,i+1):
        if a==0 or a==i:
            print("*",end=" ")
        else:
            if i==n:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print("\r")
#câu a
n = int(input("Nhập vào chiều cao:"))
k = 2*n-2
for i in range(0,n+1):
    for a in range(0,k+1):
        print(end=' ')
    k-=1
    for a in range(0,i+1):
        if a==0 or a==i:
            print("*",end=" ")
        else:
            if i==n:
                print("*",end=" ")
            else:
                print("*",end=" ")
    print("\r")
#Câu b
n = int(input("Nhập vào chiều cao:"))
k = 2*n-2
for i in range(0,n+1):
    for a in range(0,k+1):
        print(end='  ')
    k-=1
    for a in range(0,i+1):
        if a==0 or a==i:
            print("*",end="  ")
        else:
            if i==n:
                print("*",end="  ")
            else:
                print(" ",end="  ")
    print("\r")
