#c
h = int(input("Nhập chiều cao tam giác cân: "))
khoang_cach = h
for i in range(1, h+1):
    for j in range(khoang_cach):
        print(end =" ")
    khoang_cach -= 1
    for n in range(1, i+1):
        if n == h or i != h/2:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()