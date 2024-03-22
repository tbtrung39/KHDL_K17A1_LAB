# Nhập số hàng từ người dùng
n = int(input("Nhập số hàng của tam giác cân: "))

# Vẽ tam giác cân rỗng
for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    if j==3:
        print("", end="")
    if i == 0 or i == n-1 :
        print('*'*(2*i)+'*',end='')
    else:
        print('*'+' '*(2*i-1)+'*',end='')
    print()

#Vẽ tam giác đều kín
for i in range(n):
    for j in range(n-i-1):
        print(" ", end=" ")
    for j in range(2*i+1):
        print("*", end=" ")
    print()


# Vẽ tam giác đều hở
for i in range(n):
    for j in range(n-i-1):
        print(" ", end=" ")
    for j in range(2*i+1):
        if j == 0 or j == 2*i or i == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()