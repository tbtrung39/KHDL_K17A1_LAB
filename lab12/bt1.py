while True:
    try:
        a = float(input("nhap canh a: "))
        b = float(input("nhap canh b: "))
        c = float(input("nhap canh c: "))
        if a <= 0 or b <= 0 or c <= 0:
            raise BaseException("gia tri cua ca canh tam giac phai lon hon 0")
        assert a + b > c and a + c > b and b + c > a, "gia tri cac canh khong bang tong 2 canh con lai"
    except ValueError as value_error:
        print("yeu cau nhap vao so thuc")
    except AssertionError as assertion_error:
        print(assertion_error)
    except BaseException as base_error:
        print(base_error)
    else:
        print("ba canh thoa man dieu kien tam giac")
        P = (a + b + c) / 2
        S = ((P * (P - a) * (P - b) * (P - c)) ** (1/2))
        print(f"dien tich tam giac la: {S}")
        break
    finally:
        print("yeu cau nhap lai")