#
n = 5
for i in range(1, n+1):
    for j in range(1, 2*n):
        if i == n or i + j == n + 1 or j - i == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
#
n = 5

for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for j in range(2*i+1):
        if i == n-1 or j == 0 or j == 2*i:
            print("*", end="")
        else:
            print(" ", end="")
    print()
#
n = 5

for i in range(n):
    for j in range(2*n):
        if j >= n-i and j <= n+i:
            print("*", end="")
        else:
            print(" ", end="")
    print()