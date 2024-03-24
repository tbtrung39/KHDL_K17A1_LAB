n = int(input("Nhập số n: "))

list_nt = []

for num in range(2, n + 1):
    nt = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            nt = False
            break
    if nt:
        list_nt.append(num)

print("Các số nguyên tố nhỏ hơn hoặc bằng", n, "là:")
print(list_nt)
