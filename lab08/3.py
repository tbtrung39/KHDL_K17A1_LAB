def so_nguyen_to(x):
    if x<2:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    else:
        return True
n=int(input("Nhập n:"))
for j in range(n):
    if so_nguyen_to(j):
        print(f"Sô nguyên tố nhỏ hơn {n} là:",j)