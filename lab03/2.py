n=int(input("Nhập N:"))
for i in range(1,n):
  tong=0
for j in range(1,i):
     if i%j==0:
        tong+=j
if tong==i:
 print("Đây là số hoàn hảo",i)