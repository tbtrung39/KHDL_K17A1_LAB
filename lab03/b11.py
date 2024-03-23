n = int(input("nhập số hàng: "))
k = 2
for row in range (1,n+1):
    for col in range(1,n*2):
        if row+col == n+1 or col-row ==n-1:
            print("*", end="")
        elif row ==n and col != k:
            print("*", end = "")
            k=k+2
        else:
            print(end=" ")
    print()

h=int(input("Nhập chiều cao của tam giác là"))
k=2*h-2
for dong in range (1,h+1):
    for cot in range (1,k+1):
        print (end=" ")
    for cot in range (1,dong+1):
        print("*",end=" ")
    k=k-1
    print("\r")

n = int(input("Nhập chiều cao : "))
for i in range(1,n+1):
    for j in range(1,2*n):
        if i == n or j == n-i+1 or j == n+i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print("")