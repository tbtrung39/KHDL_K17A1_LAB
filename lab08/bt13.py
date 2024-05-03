def tinh_nam(y):
    if y % 4 == 0 and ( y % 100 != 0 or y % 400 != 0):
        return True
    else:
        return False
y = int(input("Nhập năm: "))
if tinh_nam(y):
    print(f"Năm {y} là năm nhuận")
else:
    print(f"Năm {y} không phải năm nhuận")
def tinh_ngay(n):
    if n <= 12 and n >=1:
        if n == 4 or n == 6 or n == 9 or n == 11:
            print(f"Tháng {n} có 30 ngày ")
        elif n == 2:
            print(f"Tháng {n} có 28 hoặc 29 ngày")
        else:
            print(f"Tháng {n} có 31 ngày")
        return True
    else:
        return False
n = int(input("Nhập tháng: "))
if tinh_ngay(n):
    pass
else:
    print("Không tồn tại tháng này")