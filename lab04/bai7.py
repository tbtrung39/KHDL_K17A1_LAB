#bài 7 
a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))
boi_chung_nho_nhat = 0
m = a
n = b
while n != 0:
    m = n
    n = m % n
boi_chung_nho_nhat = (a * b) // m
print("Bội chung nhỏ nhất của", a, "và", b, "là:", boi_chung_nho_nhat)
