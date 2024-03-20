n = int(input("Nhập chiều cao tam giác: "))
for i in range(1,n+1):
    for j in range(1,2*n):
        if i == n or j == n-i+1 or j == n+i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print("")
k = 2
for i in range(1,n+1):
    for j in range(1,n*2):
        if i+j == n+1 or j-i == n-1:
            print("*", end="")
        elif i ==n and j != k:
            print("*", end="")
            k = k + 2
        else:
            print(end=" ")
    print("")
for i in range(n):
    print(" "*(n-i-1), end="")
    for j in range(i+1):
        print("* ", end="")
    print("")