n = int(input("nhap vao mot so nguyen duong: "))
if n <= 0:
    print("Vui lòng nhập số nguyên dương.")
else:
    i = 2
    lst = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            lst.append(i)
    if n > 1:
        lst.append(n)

    print("Dạng phân tích thừa số nguyên tố của", n, "là:", lst)