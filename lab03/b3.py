so_nguyen_to = int(input("Nhập số nguyên là: "))
while True:
    for i in range(2,so_nguyen_to):
        if so_nguyen_to % i == 0:
            print(f"{so_nguyen_to} không phải là số nguyên tố")
            so_nguyen_to = so_nguyen_to - 1
            break
    else:
        print(f"{so_nguyen_to} là số nguyên tố")
        break