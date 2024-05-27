def chuyen_doi_he_co_so():
    try:
        n = int(input("Nhập một số nguyên: "))
    except ValueError:
        print("Đây không phải là một số nguyên hợp lệ.")
        return

    print("Số nguyên bạn vừa nhập là:", n)

    binary = bin(n)
    print("Số nguyên", n, "sau khi chuyển sang hệ nhị phân là:", binary)

    octal = oct(n)
    print("Số nguyên", n, "sau khi chuyển sang hệ cơ số 8 là:", octal)

    hexadecimal = hex(n)
    print("Số nguyên", n, "sau khi chuyển sang hệ cơ số 16 là:", hexadecimal)