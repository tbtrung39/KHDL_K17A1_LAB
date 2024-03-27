n = int(input("Nhập giá trị của a: "))
for i in range(0,n+1):
    if n == 0 or n == 1:
        continue
    if n % 2 == 0:
        print(f"{n} không phải là số nguyên tố")
        print(f"Số nguyên tố gần {n} nhất:")
        break
else:
    print(f"{n} là số nguyên tố")