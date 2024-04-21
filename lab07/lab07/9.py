while True:
    try:
        n = int(input("Nhập số tự nhiên n: "))
        if n >= 0:
            break
        else:
            print("Vui lòng nhập số tự nhiên không âm.")
    except ValueError:
        print("Vui lòng chỉ nhập số tự nhiên.")
A = set()
for i in range(1, n + 1):
    la_nguyen_to = True
    if n % i == 0:
        if i == 1:
            la_nguyen_to = False
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                la_nguyen_to = False
                break
        if la_nguyen_to:
            A.add(i)
B = set()
for i in range(2, n):
    la_nguyen_to = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            la_nguyen_to = False
            break
    if la_nguyen_to and n % i != 0:
        B.add(i)
print("Tập hợp A:", A)
print("Tập hợp B:", B)