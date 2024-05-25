print("Bài 3: Tìm UCLN và BCNN của hai số và tổng các ước của một số")

a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
n = int(input("Nhập số để tính tổng các ước: "))

from package import so_hoc

print("Ước chung lớn nhất là:", so_hoc.Ucln(a, b))
print("Bội chung nhỏ nhất là:", so_hoc.Bcnn(a, b))
print(f"Tổng các ước của {n} là {so_hoc.SumDivisor(n)}")