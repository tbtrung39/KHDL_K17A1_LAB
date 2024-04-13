n = int(input("Nhap so phan tu cua day : "))
fib_list = [0, 1] + [fib_list[i-1] + fib_list[i-2] for i in range(2, n)]
print(fib_list)


