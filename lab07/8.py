def la_so_thuc(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

A = set()
while True:
    n = input("Nhập vào phần tử cho tập A (nhấn ESC để thoát): ")
    if n.upper() == "ESC":
        break
    A.add(n)

so_nguyen = 0
so_thuc = 0
ki_tu = 0

for i in A:
    if i.isdigit():
        so_nguyen += 1
    elif la_so_thuc(i):
        so_thuc += 1
    elif i.isalpha():
        ki_tu += 1

print("Số phần tử là số nguyên:", so_nguyen)
print("Số phần tử là số thực:", so_thuc)
print("Số phần tử là kí tự:", ki_tu)