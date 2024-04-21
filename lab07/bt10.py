m = eval(input("Nhập số tự nhiên: "))
n = eval(input("Nhập số tự nhiên: "))
m = set(m) ; n = set(n)
f = m.intersection(n)
print("Các chữ số chung: ",f)
tong = 0
for i in f:
    tong += i
print("Tổng các chữ số chung của m và n: ",tong)