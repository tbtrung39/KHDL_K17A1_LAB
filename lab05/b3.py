n = input("Nhập số nguyên dương n: ")
if n.isdigit():
    n = int(n)
    if n >= 0:
        if n == 0:
            print("Số nhị phân của 0 là: 0")
        else:
            nhi_phan = ""
            while n > 0:
                nhi_phan = str(n % 2) + nhi_phan
                n = n // 2
            print("Số nhị phân là:", nhi_phan)
    else:
        print("Vui lòng nhập một số nguyên dương.")
else:
    print("Vui lòng nhập một số nguyên dương.")
