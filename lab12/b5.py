def tinh_S1(n):
    if n < 0:
        raise ValueError("Giá trị n không được âm.")
    elif n == 0:
        return 0
    else:
        return n + tinh_S1(n - 1)

def tinh_S2(n):
    if n < 0:
        raise ValueError("Giá trị n không được âm.")
    elif n == 0:
        return 0
    else:
        return n**2 + tinh_S2(n - 1)

try:
    n = int(input("Nhập giá trị n: "))

    S1 = tinh_S1(n)
    S2 = tinh_S2(n)

    print("Tổng S1 =", S1)
    print("Tổng S2 =", S2)

except ValueError:
    print("Lỗi: Bạn cần nhập một số nguyên.")
except RecursionError:
    print("Lỗi: Giá trị quá lớn, không thể tính toán.")
except Exception as e:
    print("Lỗi không xác định:", e)
