def tinh_S1(n):
    if n <= 0:
        raise ValueError("n khong phai so nguyen duong!!!")
    if n == 1:
        return 1
    else:
        return n + tinh_S1(n - 1)

def tinh_S2(n):
    if n <= 0:
        raise ValueError("n khong phai so nguyen duong!!!")
    if n == 1:
        return 1
    else:
        return n ** 2 + tinh_S2(n - 1)

try:
    n = int(input("nhap n: "))
    S1 = tinh_S1(n)
    S2 = tinh_S2(n)

    print(f"S1 = {S1}")
    print(f"S2 = {S2}")

except ValueError as e:
    print(f"loi: {e}")
except RecursionError:
    print("loi: n qua lon khong xu ly duoc")
except Exception as f:
    print(f"loi khong xac dinh: {f}")
