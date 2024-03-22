n=int(input("Nhập số nguyên n:"))
tong=0
if n<=0:
  print("Nhập lại n")
else:
  for i in range (1,n+1):
   tong+=1/i
  print("Tổng=",tong)