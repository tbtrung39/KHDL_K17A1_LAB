# 1 a
n = int(input("nhập số n:"))
sum = 0
if n < 0:
   print("vui lòng thử lại")
else:
   while True:
      for i in range(1,n+1):
         sum += i
         b = pow(sum,2)
      print(b)
      break
#1b
n = int(input("Nhập n: "))
S = 0

if n < 0:
    print("Vui lòng thử lại")
else:
    while True:
        for i in range(1, 2*n + 2, 2):
            S += i**3
        print("Tổng S là:", S)
        break
#1c
n = int(input("nhập số n:"))
sum = 0
if n < 0:
    print("vui lòng thử lại")
else:
    while True:
        for i in range(1,2*n,2):
            sum += i**4
        print("tổng của c là ", sum)
        break