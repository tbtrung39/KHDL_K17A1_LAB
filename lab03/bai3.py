n = int(input("Nhập một số nguyên dương n: "))
flag = True
for i in range(2, n ):
    if n % i == 0:
        flag = False
        break

if flag:
    print(f"{n} là số nguyên tố.")
else:
    print(f"{n} không là số nguyên tố.")
so = ()
for i in range(n - 1, 1, -1):
    flag = True
    for j in range(2,  i):
        if i % j == 0:
            flag = False
            break
    if flag:
        so = i
        break

if so:
    print(f"Số nguyên tố gần nhất với {n} là: {so}")
else:
    print(f"Không có số nguyên tố nào gần {n}.")