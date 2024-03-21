# tính tổng s = 1/1 -1/2 + 1/3-1/4 + 1/5-.....
n = int(input("Nhập n: "))
S = 0
a = 1
if n < 0:
    print("vui lòng nhập lại")
else:
    while True:
        for i in range(1, n+1):
            S += a * (1/i)
            a = -a
        print("Tổng S là:", S)
        break

# tính tổng s = 1/1 -1/2 + 1/3-1/4 + 1/5-.....
n = int(input("Nhập n: "))
S = 0
a = 1
if n < 0:
    print("vui lòng nhập lại")
else:
    while True:
        for i in range(1, n+1):
            S += a * (1/i)
            a = -a
        print("Tổng S là:", S)
        break

# tính tổng 1 phần căn
import math 
n = int(input("nhập số n:"))
sum = 0
if n < 0:
    print("vui lòng nhập lại")
else:
    while True:
        for i in range(1, n+1):
            sum += i*(1/math.sqrt(i))
        print("tổng các số căn là",sum)
        break