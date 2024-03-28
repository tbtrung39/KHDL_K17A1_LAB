a = int(input("Nhập vào a:"))
b = int(input("Nhập vào b:"))
x,y=a,b
while x!=y:
    if x>y:
        x=x-y
    else:
        y=y-x
print(f"bội chung nhỏ nhất của {a} và {b} là {a*b/x}")