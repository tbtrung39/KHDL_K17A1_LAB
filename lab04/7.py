# tìm bội chung nhỏ nhất của 2 số nguyên vừa nhập từ bàn phím 
import math
n = int(input("nhập số nguyên thứ nhất:"))
m = int(input("nhập số nguyên thứ hai :"))
while True: 
    x = math.gcd(n,m)
    print("bội chung nhỏ nhất của số nguyên thứ nhất và số nguyên thứ hai là",x)
    break
    