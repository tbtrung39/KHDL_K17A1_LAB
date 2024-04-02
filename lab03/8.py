n=int(input("Nhập số nguyên n:"))
tong=0
if n<=0:
  print("Nhập lại n")
else:
  for i in range (1,n+1):
   tong+=i
  print("Tổng=",tong)

n=int(input("Nhập số nguyên n:"))
tong=0
if n<=0:
  print("Nhập lại n")
else:
  for i in range (1,n+1,2):
   tong+=i
  print("Tổng=",tong)

n=int(input("Nhập số nguyên n:"))
tong=0
if n<=0:
  print("Nhập lại n")
else:
  for i in range (2,n+1,2):
   tong+=i
  print("Tổng=",tong)