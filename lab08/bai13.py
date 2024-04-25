def check_year(y):
    if y % 4 == 0 and ( y % 100 != 0 or y % 400 != 0):
        return True
    else:
        return False
y = int(input("nhập vào năm cần xác định: "))
if check_year(y):
    print(f"năm {y} là năm nhuận")
else:
    print(f"năm {y} không phải năm nhuận")
def check_days(n):
    if n <= 12 and n >=1:
        if n == 4 or n == 6 or n == 9 or n == 11:
            print(f"tháng {n} có 30 ngày ")
        elif n == 2:
            print(f"tháng {n} có 28 hoặc 29 ngày")
        else:
            print(f"tháng {n} có 31 ngày")
        return True
    else:
        return False
n = int(input("nhập vào tháng cần xác định: "))
if check_days(n):
    pass
else:
    print("không tồn tại tháng này")